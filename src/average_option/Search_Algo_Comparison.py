import time
import multiprocessing
from AverageOption_CRR import average_Call_CRR, average_Call_CRR_binary, average_Call_CRR_interpolation

# arithmetic average call
# payoff = max(Save,τ − K, 0)

# time_elapsed ------> t
# time_left_to_Maturity ------> T - t




# main
StInit = 50
StAve = 50
K = 50
r = 0.1
q = 0.05
sigma = 0.8
time_left_to_maturity = 0.25
M = 100
layers_prev = 100
layers = 100


if __name__ == '__main__':
    # sequential search
    start = time.perf_counter()

    print('============================================================')
    print('{ Sequential Search }')
    time_elapsed = 0
    type = 'European'
    p1 = multiprocessing.Process(target = average_Call_CRR, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])
    type = 'American'
    p2 = multiprocessing.Process(target = average_Call_CRR, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])

    time_elapsed = 0.25
    type = 'European'
    p3 = multiprocessing.Process(target = average_Call_CRR, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])
    type = 'American'
    p4 = multiprocessing.Process(target = average_Call_CRR, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])

    processes = [p1, p2, p3, p4]
    for process in processes:
        process.start()
    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f'Process finished in {round(finish - start, 2)} second(s).')
    print('\n')


    # binary search
    start = time.perf_counter()

    print('============================================================')
    print('{ Binary Search }')
    time_elapsed = 0
    type = 'European'
    p5 = multiprocessing.Process(target = average_Call_CRR_binary, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])
    type = 'American'
    p6 = multiprocessing.Process(target = average_Call_CRR_binary, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])

    time_elapsed = 0.25
    type = 'European'
    p7 = multiprocessing.Process(target = average_Call_CRR_binary, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])
    type = 'American'
    p8 = multiprocessing.Process(target = average_Call_CRR_binary, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])

    processes = [p5, p6, p7, p8]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    
    finish = time.perf_counter()
    print(f'Process finished in {round(finish - start, 2)} second(s).')
    print('\n')


    # interpolation search
    start = time.perf_counter()

    print('============================================================')
    print('{ Interpolation Search }')
    time_elapsed = 0
    time_elapsed = 0
    type = 'European'
    p9 = multiprocessing.Process(target = average_Call_CRR_interpolation, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])
    type = 'American'
    p10 = multiprocessing.Process(target = average_Call_CRR_interpolation, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])

    time_elapsed = 0.25
    type = 'European'
    p11 = multiprocessing.Process(target = average_Call_CRR_interpolation, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])
    type = 'American'
    p12 = multiprocessing.Process(target = average_Call_CRR_interpolation, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])

    processes = [p9, p10, p11, p12]
    for process in processes:
        process.start()
    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f'Process finished in {round(finish - start, 2)} second(s).')
    print('\n')