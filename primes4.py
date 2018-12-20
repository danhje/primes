import time
import math


starttime = time.time()
primes_list = []

def prime(num):
	for o in range(2, int(math.ceil(math.sqrt(num)))+1):
		if num%o == 0:
			break
	else:
			return num


primes_list = [2] + map(prime, range(3, 10000, 2))
for i in range(primes_list.count(None)):
	primes_list.remove(None)

print primes_list
print "\n", len(primes_list), "primtall funnet."
endtime = time.time()
print "Det tok", endtime - starttime, "s.\n"
