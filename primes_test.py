'''
@author: Daniel Hjertholm
'''


import time
import numpy as np
import matplotlib.pyplot as plt
from algorithms.primes1 import primes as p1
from algorithms.primes2 import primes as p2
from algorithms.primes3 import primes as p3
from algorithms.primes4 import primes as p4
from algorithms.primes5 import primes as p5
from algorithms.primes6 import primes as p6
from algorithms.primes7 import primes as p7
from algorithms.primes8 import primes as p8

num_algorithms = 8
start = 100
stop = 10000
step = 100
ubounds = range(0, 10000, 100)
num = len(ubounds)

results = []

for i in range(1, num_algorithms+1):
    print('Testing algorithm', i)
    results_for_current_algorithm = []
    for ubound in ubounds:
        starttime = time.time()
        result = eval('p' + str(i) + '(ubound)')
        endtime = time.time()
        duration = endtime - starttime
        #print(len(result), "primes found in", duration, "seconds.")
        results_for_current_algorithm.append(duration)
    results.append(results_for_current_algorithm)

plt.plot(np.transpose(np.array(results)), linewidth=2)
plt.xticks(range(len(ubounds))[0::10], ubounds[0::10])
plt.xlabel('Upper bound for primes')
plt.ylabel('Time in seconds to generate primes')
plt.legend(['algorithm 1', 'algorithm 2', 'algorithm 3', 'algorithm 4',
            'algorithm 5', 'algorithm 6', 'algorithm 7', 'algorithm 8'], loc=2)
plt.show()
