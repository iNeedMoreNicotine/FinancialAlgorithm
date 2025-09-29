from math import log, exp, sqrt
import numpy as np
import time
import multiprocessing
# payoff = max(Smax,τ − Sτ , 0)

def lookback_EuroPut_MC(StMax, St, time_left_to_maturity, r, q, sigma, n, sims, rep, print_out = False):
    dt = time_left_to_maturity/n
    times = 0
    means = []
    means = np.ndarray(shape = (rep))
    while times < rep:
        optionValues = np.ndarray(shape = (sims))

        for sim in range(sims):
            stockPrices = np.ndarray(shape = (n+1))
            stockPrices[0] = log(St)
            for i in range(n):
                dlnS = np.random.normal(loc = (r-q-sigma**2/2)*dt, scale = sigma*sqrt(dt))
                stockPrices[i+1] = dlnS
            
            stockPrices = np.cumsum(stockPrices)
            stockPrices = np.exp(stockPrices)
            
            if StMax == St:
                maxPrice = max(stockPrices)
            else:
                maxPrice_after_t = max(stockPrices)
                maxPrice = max(StMax, maxPrice_after_t)

            putValue = max(maxPrice - stockPrices[-1], 0) * exp(-r * time_left_to_maturity)
            optionValues[sim] = putValue

        mean = np.mean(optionValues)
        means[times] = mean
        times += 1

    sdOfRep = np.std(means)
    meanOfRep = np.mean(means)
    upperBound = meanOfRep + 2*sdOfRep
    upperBound = round(upperBound, 4)
    lowerBound = meanOfRep - 2*sdOfRep
    lowerBound = round(lowerBound, 4)
    bounds = [lowerBound, upperBound]

    if print_out == True:
        print(f'(MC) Mean price of European Lookback Put (Smax,t = {StMax}): {round(meanOfRep, 4)}')
        print(f"     Standard Error : {round(sdOfRep, 4)}")
        print(f"     95% Confidence Interval : {bounds}")

    return meanOfRep




# # main
# St = 50
# T = 0.25
# r = 0.1
# q = 0
# sigma = 0.4
# n = 100
# sims = 10000
# reps = 20

# StMax = 50
# lookback_EuroPut_MC(StMax, St, T, r, q, sigma, n, sims, reps)
# StMax = 60
# lookback_EuroPut_MC(StMax, St, T, r, q, sigma, n, sims, reps)
# StMax = 70
# lookback_EuroPut_MC(StMax, St, T, r, q, sigma, n, sims, reps)

# start = time.perf_counter()

# if __name__ == '__main__':
#     StMax = 50
#     p1 = multiprocessing.Process(target = lookback_EuroPut_MC, args = [StMax, St, T, r, q, sigma, n, sims, reps])
#     StMax = 60
#     p2 = multiprocessing.Process(target = lookback_EuroPut_MC, args = [StMax, St, T, r, q, sigma, n, sims, reps])
#     StMax = 70
#     p3 = multiprocessing.Process(target = lookback_EuroPut_MC, args = [StMax, St, T, r, q, sigma, n, sims, reps])

#     p1.start()
#     p2.start()
#     p3.start()
#     p1.join()
#     p2.join()
#     p3.join()
#     finish = time.perf_counter()
#     print(f'Process finished in {round(finish - start, 2)} second(s).')