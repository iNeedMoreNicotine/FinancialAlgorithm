# Monte Carlo
from math import log, exp, sqrt
from scipy.stats import norm
import numpy as np

def European_MC(S0, K, T, r, q, sigma, call_put, sims, rep, print_out = False):
    meanValueLst = []
    times = 0
    while times < rep:
        stockSamples = []
        for i in range(sims):
            # stockSamples.append(S0 * exp((r - q - 0.5 * sigma**2) * T + sigma * sqrt(T) * np.random.standard_normal()))
            # lnSample = log(S0) + (r - q - 0.5*sigma**2) * T + sigma * sqrt(T) * np.random.standard_normal()
            lnSample = np.random.normal(loc = log(S0) + (r - q - 0.5*(sigma**2))* T, scale = sigma * sqrt(T))
            sample = exp(lnSample)
            stockSamples.append(sample)
        
        optionValue = []
        if call_put == "call":
            for price in stockSamples:
                optionValue.append(max(price-K, 0))

            meanValue = np.mean(optionValue)
            discounted = meanValue * exp(-r * T)
            meanValueLst.append(discounted)
            times += 1

        else:
            for price in stockSamples:
                optionValue.append(max(K-price, 0))

            meanValue = np.mean(optionValue)
            discounted = meanValue * exp(-r * T)
            meanValueLst.append(discounted)
            times += 1

    sdOfRep = np.std(meanValueLst)
    meanOfRep = np.mean(meanValueLst)
    upperBound = meanOfRep + 2*sdOfRep
    upperBound = round(upperBound, 4)
    lowerBound = meanOfRep - 2*sdOfRep
    lowerBound = round(lowerBound, 4)
    bounds = [lowerBound, upperBound]

    if print_out == True:
        print(f'(MC) Mean price of European {call_put}: {round(meanOfRep, 4)}')
        print(f"     Standard Error : {round(sdOfRep, 4)}")
        print(f"     95% Confidence Interval : {bounds}")

    return meanOfRep

# S0 = 115
# K = 115
# r = 0.01
# q = 0.02
# sigma = 0.5
# T = 1
# sims = 10000
# rep = 20
# European_MC(S0, K, T, r, q, sigma, "call", sims, rep)
# European_MC(S0, K, T, r, q, sigma, "put", sims, rep)