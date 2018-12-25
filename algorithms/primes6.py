'''
@author: Daniel Hjertholm
'''



import math

def primes(ubound):
    '''
    Takes every odd number up to ubound and tests for primality. Tests for
    primality by checking the remainder after dividing with the primes already
    found that are smaller than the square root of the number being checked.
    '''
    primes_list = [2]
    for i in range(3, ubound, 2):
        primes_list_sub = [elem for elem in primes_list if elem <= math.sqrt(i)]
        for o in primes_list_sub:
            if i%o == 0:
                break
        else:
            primes_list.append(i)
    return primes_list



if __name__ == "__main__":
    import time
    starttime = time.time()
    result = primes(10000)
    endtime = time.time()
    print(len(result), "primes found in", endtime - starttime, "seconds.")
