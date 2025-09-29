'''
(1) Vanilla Option 
'''
from src.vanilla_option.Option_BlackScholes import BlackScholes
from src.vanilla_option.Option_MonteCarlo import European_MC
from src.vanilla_option.Option_BinomialTree import European_CRR, American_CRR, European_CRR_Combinatorial


S0 = 100
K = 110
r = 0.01
q = 0.02
sigma = 0.5
T = 1

print('='*60)
print('(1) VANILLA OPTION')

# BlackScholes
print('-'*60)
print('European Option : Black-Scholes Model')
print('-'*60)
BlackScholes(S0, K, T, r, q, sigma, "call", print_out = True)
BlackScholes(S0, K, T, r, q, sigma, "put", print_out = True)
print()

# Monte Carlo
sims = 50000
rep = 20
print('-'*60)
print('European Option : Monte Carlo')
print('-'*60)
European_MC(S0, K, T, r, q, sigma, "call", sims, rep, print_out = True)
European_MC(S0, K, T, r, q, sigma, "put", sims, rep, print_out = True)
print()

# Binomial Tree
layers = 2000
print('-'*60)
print('European & American Option : Binomial Tree')
print('-'*60)
# European Option
European_CRR(S0, K, T, r, q, sigma, layers, "call", print_out = True)
European_CRR(S0, K, T, r, q, sigma, layers, "put", print_out = True)
# American Option
American_CRR(S0, K, T, r, q, sigma, layers, "call", print_out = True)
American_CRR(S0, K, T, r, q, sigma, layers, "put", print_out = True)
# European Option (combinatorial method)
European_CRR_Combinatorial(S0, K, T, r, q, sigma, layers, 'call', print_out = True)
European_CRR_Combinatorial(S0, K, T, r, q, sigma, layers, 'put', print_out = True)
print()

# --- Financial Interpretation ---
print("Summary:")
print("- Black-Scholes (closed-form), Monte Carlo, and Binomial Tree all yield consistent results.")
print("- American options are slightly more valuable than European ones due to early exercise flexibility.\n")
print('\n')




'''
(2) Rainbow Option 
'''
'''
parameters of call_put:
call on max: max(max(S1, S2, ..., Sn) - K, 0)
call on min: max(min(S1, S2, ..., Sn) - K, 0)
put on max: max(K - max(S1, S2, ..., Sn), 0)
put on min: max(K - min(S1, S2, ..., Sn), 0)
'''
from src.rainbow_option.RainbowOption_MonteCarlo import rainbow_MC
from src.rainbow_option.RainbowOption_AntitheticVariate_MomentMatching import rainbow_MC_AntitheticVariate


asset_amount = 5
S0_lst = [100, 100, 100, 100, 100]
K = 110
T = 1
r = 0.01
q_lst = [0.05, 0.04, 0.06, 0.03, 0.04]
sigma_lst = [0.5, 0.5, 0.5, 0.5, 0.5]
rho_dict = {'rho12': 0.5, 'rho13': 0.4, 'rho14': 0.3, 'rho15': 0.2, 'rho23':0.5, 'rho24':0.4, 'rho25':0.3, 'rho34':0.5, 'rho35':0.4, 'rho45':0.3}
sims = 30000
reps = 20

print('='*60)
print('(2) RAINBOW OPTION')

# Monte Carlo
print('-'*60)
print('European Rainbow Option : Monte Carlo')
print('-'*60)
rainbow_MC(asset_amount, S0_lst, K, T, r, q_lst, sigma_lst, rho_dict, sims, reps, 'call on max', print_out = True)
rainbow_MC(asset_amount, S0_lst, K, T, r, q_lst, sigma_lst, rho_dict, sims, reps, 'call on min', print_out = True)
rainbow_MC(asset_amount, S0_lst, K, T, r, q_lst, sigma_lst, rho_dict, sims, reps, 'put on max', print_out = True)
rainbow_MC(asset_amount, S0_lst, K, T, r, q_lst, sigma_lst, rho_dict, sims, reps, 'put on min', print_out = True)
print()

# Monte Carlo with Variance-Reduction Technique
print('-'*60)
print('European Rainbow Option : Monte Carlo with Variance-Reduction')
print('-'*60)
rainbow_MC_AntitheticVariate(asset_amount, S0_lst, K, T, r, q_lst, sigma_lst, rho_dict, sims, reps, 'call on max', print_out = True)
rainbow_MC_AntitheticVariate(asset_amount, S0_lst, K, T, r, q_lst, sigma_lst, rho_dict, sims, reps, 'call on min', print_out = True)
rainbow_MC_AntitheticVariate(asset_amount, S0_lst, K, T, r, q_lst, sigma_lst, rho_dict, sims, reps, 'put on max', print_out = True)
rainbow_MC_AntitheticVariate(asset_amount, S0_lst, K, T, r, q_lst, sigma_lst, rho_dict, sims, reps, 'put on min', print_out = True)
print()

# --- Financial Interpretation ---
print("Summary:")
print("- Rainbow options depend on multiple assets (here, 5 underlyings).")
print("- The 'call on max' is valuable because it benefits from the best-performing asset.")
print("- Variance-reduction significantly reduces estimation error (narrower confidence intervals).\n")
print('\n')




'''
(3) Lookback Option 
'''
from src.lookback_option.LookbackOption_MonteCarlo import lookback_EuroPut_MC
from src.lookback_option.LookbackOption_CRR import lookback_Put_CRR
from src.lookback_option.LookbackOption_CheukAndVorst import lookback_Put_CRR_CheukAndVorst


StMax = 110
St = 100
r = 0.01
q = 0.02
sigma = 0.5
n = 100
T = 1

print('='*60)
print('(3) LOOKBACK OPTION')

# Monte Carlo
'''
Only European lookback put is implemented
payoff = max(Smax,τ - Sτ , 0)
'''
sims = 10000
reps = 20
print('-'*60)
print('European Lookback Put : Monte Carlo')
print('-'*60)
lookback_EuroPut_MC(StMax, St, T, r, q, sigma, n, sims, reps, print_out = True)
print()

# Binomial Tree
'''
Only lookback put is implemented
'''
layers = 100
print('-'*60)
print('European & American Lookback Put : Binomial Tree')
print('-'*60)
lookback_Put_CRR(StMax, St, T, r, q, sigma, layers, 'European', print_out = True)
lookback_Put_CRR(StMax, St, T, r, q, sigma, layers, 'American', print_out = True)
print()

# Binomial Tree (Method from Cheuk and Vorst (1997))
print('-'*60)
print('European & American Lookback Put : Binomial Tree (Cheuk and Vorst (1997))')
print('-'*60)
lookback_Put_CRR_CheukAndVorst(St, T, r, q, sigma, layers, 'European', print_out = True)
lookback_Put_CRR_CheukAndVorst(St, T, r, q, sigma, layers, 'American', print_out = True)
print()

# --- Financial Interpretation ---
print("Summary:")
print("- Lookback options let the payoff depend on the maximum/minimum reached during the option's life.")
print("- The lookback put is more valuable than a plain put, since it allows exercise against the historical maximum.\n")
print('\n')




'''
(4) Average Option 
'''
from src.average_option.AverageOption_MonteCarlo import average_EuroCall_MC
from src.average_option.AverageOption_CRR import average_Call_CRR


St = 50
StAve = 50
K = 50
r = 0.1
q = 0.05
sigma = 0.8
time_elapsed = 0.25
time_left_to_maturity = 0.25

print('='*60)
print('(4) AVERAGE OPTION')

# Monte Carlo
'''
Only European arithmetic average call is implemented
payoff = max(Save,τ - K, 0)

time_elapsed -----> t
time_left_to_Maturity -----> T - t
'''
sims = 10000
rep = 20
n_prev = 100
n = 100
print('-'*60)
print('European Average Call : Monte Carlo')
print('-'*60)
average_EuroCall_MC(StAve, St, K, time_elapsed, time_left_to_maturity, r, q, sigma, n_prev, n, sims, rep, print_out = True)
print()

# Binomial Tree
'''
Only average call is implemented
'''
M = 100
layers_prev = 100
layers = 100
log_arrayed = True
print('-'*60)
print('European & American Average Call : Binomial Tree')
print('-'*60)
average_Call_CRR(StAve, St, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, 'European', log_arrayed, print_out = True)
average_Call_CRR(StAve, St, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, 'American', log_arrayed, print_out = True)
print()
print('For comparison of different search algorithm used in implementing the pricing of average option (with CRR Model),\nplease refer to src/average_option/Search_Algo_Comparison.py')
print()

# --- Financial Interpretation ---
print("Summary:")
print("- Asian options depend on the average price, which smooths volatility.")
print("- As a result, the Asian call is priced lower than a comparable vanilla call.\n")




'''
(5) Implied Volatility
'''
'''
Compute "implied volatility" of underlying assets using the market price of the option
'''
from src.implied_volatility.ImpliedVolatility import iv_bisection, iv_newton


S0 = 50
K = 55
r = 0.1
q = 0.03
T = 0.5

print('='*60)
print('(5) IMPLIED VOLATILITY')

# Bisection Method
marketPrice = 2.5
print('-'*60)
print('Calculating IV using bisection method')
print('-'*60)
marketPrice = 6.5
iv_bisection(marketPrice, S0, K, T, r, q, call_put = "put", type = "American", model = "BS", layers = None, converCrit = 10**(-6), print_out = True)
iv_bisection(marketPrice, S0, K, T, r, q, call_put = "put", type = "American", model = "CRR", layers = 100, converCrit = 10**(-6), print_out = True)
print()

# Newton Method
print('-'*60)
print('Calculating IV using Newton method')
print('-'*60)
marketPrice = 6.5
iv_newton(marketPrice, S0, K, T, r, q, "put", type = "American", model = "BS", layers = None, converCrit = 10**(-6), print_out = True)
iv_newton(marketPrice, S0, K, T, r, q, "put", type = "American", model = "CRR", layers = 100, converCrit = 10**(-6), print_out = True)
print()

# --- Financial Interpretation ---
print("Summary:")
print("- Implied volatility is obtained by solving for the volatility that matches the market price.")
print("- Both Bisection and Newton methods converge to similar results, confirming numerical robustness.\n")

print('\n')