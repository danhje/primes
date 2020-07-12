'''
@author: Daniel Hjertholm
'''


import time
import numpy as np
import matplotlib.pyplot as plt
from algorithms import primes1, primes2, primes3, primes4, primes5, primes6, primes7, primes8


ubounds = range(0, 10000, 100)
num = len(ubounds)

results = []

for algorithm in (primes1, primes2, primes3, primes4, primes5, primes6, primes7, primes8):
    print(f'Testing algorithm {algorithm.__name__}')
    results_for_current_algorithm = []
    for ubound in ubounds:
        starttime = time.time()
        result = algorithm(ubound)
        endtime = time.time()
        duration = endtime - starttime
        results_for_current_algorithm.append(duration)
    results.append(results_for_current_algorithm)

plt.plot(np.transpose(np.array(results)), linewidth=2)
plt.xticks(range(len(ubounds))[0::10], ubounds[0::10])
plt.xlabel('Upper bound for primes')
plt.ylabel('Time in seconds to generate primes')
plt.legend(['algorithm 1', 'algorithm 2', 'algorithm 3', 'algorithm 4',
            'algorithm 5', 'algorithm 6', 'algorithm 7', 'algorithm 8'], loc=2)
plt.show()
