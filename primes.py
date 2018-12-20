import time



starttime = time.time()
primes_list = [2]



def primes(ubound):
	global primes_list
	for i in range(3, ubound, 2):
		for o in primes_list:
			if i%o == 0:
				break
		else:
			primes_list.append(i)
	return primes_list



print primes(10000)
print "\n", len(primes_list), "primtall funnet."
endtime = time.time()
print "Det tok", endtime - starttime, "s.\n"
