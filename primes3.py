import time
import math


starttime = time.time()

def is_prime(num):
        for o in range(2, int(math.ceil(math.sqrt(num)))+1):
                if num % o == 0:
                        break
        else:
                return 1

def primes(ubound):
	x = range(3, ubound, 2)
	return [2] + filter(is_prime, x)


primes_list = primes(10000)
print primes_list
print "\n", len(primes_list), "primtall funnet."
endtime = time.time()
print "Det tok", endtime - starttime, "s.\n"
