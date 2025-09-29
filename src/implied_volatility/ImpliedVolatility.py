from math import log, sqrt, exp
from scipy.stats import norm
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))
from src.vanilla_option.Option_BlackScholes import BlackScholes
from src.vanilla_option.Option_BinomialTree import European_CRR, American_CRR


# 定義損失函數 
def loss_function_BS(marketPrice, S0, K, T, r, q, sigma, call_put):
    return BlackScholes(S0, K, T, r, q, sigma, call_put) - marketPrice

def loss_function_CRR(marketPrice, S0, K, T, r, q, sigma, call_put, layers, type):
    if type == "European":
        return European_CRR(S0, K, T, r, q, sigma, layers, call_put) - marketPrice
    else:
        return American_CRR(S0, K, T, r, q, sigma, layers, call_put) - marketPrice

# 計算隱含波動度
# bisection method
def iv_bisection(marketPrice, S0, K, T, r, q, call_put, type, model, layers, converCrit, print_out = False):
    # 損失函數 < 0：市價 > BS ======> sigma應盡量取小
    # 損失函數 > 0：市價 < BS ======> sigma應盡量取大（但不要太大ㄛ）
    # 初始化區間[a, b]
    a = 0.1
    b = 1
    # 崩潰可調崩潰可調崩潰可調崩潰可調崩潰可調

    if model == "BS":
        while abs(a-b) > converCrit:
            x = a + (b-a)/2
            if loss_function_BS(marketPrice, S0, K, T, r, q, a, call_put) * loss_function_BS(marketPrice, S0, K, T, r, q, x, call_put) < 0:
                b = x
            else:
                a = x
        iv = (a + b)/2

        if print_out == True:
            print(f'IV of {type} {call_put} : {round(100*iv, 2)}% (Black-Scholes, Bisection method)')
        
        return iv

    elif model == "CRR":
        while abs(a-b) > converCrit:
            x = a + (b-a)/2
            if loss_function_CRR(marketPrice, S0, K, T, r, q, a, call_put, layers, type) * loss_function_CRR(marketPrice, S0, K, T, r, q, x, call_put, layers, type) < 0:
                b = x
            else:
                a = x
        iv = (a + b)/2

        if print_out == True:
            print(f'IV of {type} {call_put} : {round(100*iv, 2)}% (CRR, Bisection method')

        return iv

    else:
        print("invalid model!!!")
        return None

# 計算導數
def vega_bs(S0, K, T, r, q, sigma):
    # put與call的vega相同 (by put-call parity)
    d1 = (log(S0 / K) + (r - q + 0.5 * sigma **2) * T) / sigma / sqrt(T)
    vega = exp(-q*T) * S0 * sqrt(T) * norm.pdf(d1)
    return vega

def vega_binomial(S0, K, T, r, q, sigma, layers, call_put, type):
    dsigma = 10**(-8)
    if type == "European":
        price0 = European_CRR(S0, K, T, r, q, sigma, layers, call_put)
        price1 = European_CRR(S0, K, T, r, q, (sigma + dsigma), layers, call_put)

    else:
        price0 = American_CRR(S0, K, T, r, q, sigma, layers, call_put)
        price1 = American_CRR(S0, K, T, r, q, (sigma + dsigma), layers, call_put)

    vega = (price1 - price0)/dsigma
    return vega

# Newton method
def iv_newton(marketPrice, S0, K, T, r, q, call_put, type, model, layers, converCrit, print_out = False):
    x = 0.3
    if model == "BS":
        while abs(loss_function_BS(marketPrice, S0, K, T, r, q, x, call_put)) > converCrit:
            diff = vega_bs(S0, K, T, r, q, x)
            x = x - loss_function_BS(marketPrice, S0, K, T, r, q, x, call_put)/diff
        iv = x

        if print_out == True:
            print(f'IV of {type} {call_put} : {round(100*iv, 2)}% (Black-Scholes, Newton method)')

    else:
        while abs(loss_function_CRR(marketPrice, S0, K, T, r, q, x, call_put, layers, type)) > converCrit:
            diff = vega_binomial(S0, K, T, r, q, x, layers, call_put, type)
            x = x - loss_function_CRR(marketPrice, S0, K, T, r, q, x, call_put, layers, type)/diff
        iv = x

        if print_out == True:
            print(f'IV of {type} {call_put} : {round(100*iv, 2)}% (CRR, Newton method)')
    
    return iv




# # main
# S0 = 50
# K = 55
# r = 0.1
# q = 0.03
# T = 0.5


# # bisection method (checked)
# print("==========BISECTION METHOD==========")
# print("European Call")
# print("--------------------")
# marketPrice = 2.5
# iv_bisection(marketPrice, S0, K, T, r, q, call_put = "call", type = "European", model = "BS", layers = None, converCrit = 10**(-6), print_out = True)
# iv_bisection(marketPrice, S0, K, T, r, q, call_put = "call", type = "European", model = "CRR", layers = 100, converCrit = 10**(-6), print_out = True)
# print()

# print("American Put")
# print("--------------------")
# marketPrice = 6.5
# iv_bisection(marketPrice, S0, K, T, r, q, call_put = "put", type = "American", model = "BS", layers = None, converCrit = 10**(-6), print_out = True)
# iv_bisection(marketPrice, S0, K, T, r, q, call_put = "put", type = "American", model = "CRR", layers = 100, converCrit = 10**(-6), print_out = True)
# print("\n")

# # Newton method (checked)
# print("==========NEWTON METHOD==========")
# print("European Call")
# print("--------------------")
# marketPrice = 2.5
# iv_newton(marketPrice, S0, K, T, r, q, "call", type = "European", model = "BS", layers = None, converCrit = 10**(-6), print_out = True)
# iv_newton(marketPrice, S0, K, T, r, q, "call", type = "European", model = "CRR", layers = 100, converCrit = 10**(-6), print_out = True)
# print()

# print("American Put")
# print("--------------------")
# marketPrice = 6.5
# iv_newton(marketPrice, S0, K, T, r, q, "put", type = "American", model = "BS", layers = None, converCrit = 10**(-6), print_out = True)
# iv_newton(marketPrice, S0, K, T, r, q, "put", type = "American", model = "CRR", layers = 100, converCrit = 10**(-6), print_out = True)
# print("\n")