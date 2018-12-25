'''
@author: Daniel Hjertholm
'''



import math

def is_prime(num):
    for o in range(2, int(math.ceil(math.sqrt(num)))+1):
        if num % o == 0:
            break
    else:
        return num

def primes(ubound):
    '''
    Starts with list of ints up to ubound, and uses map to "None out" those
    that are not primes. Tests for primality by dividing by ints up to the
    square root of the number being tested and checking if the remainder is 0.
    '''

    primes_list = [2] + list(map(is_prime, range(3, ubound, 2)))
    for i in range(primes_list.count(None)):
        primes_list.remove(None)
    return primes_list



if __name__ == "__main__":
    import time
    starttime = time.time()
    result = primes(10000)
    endtime = time.time()
    print(len(result), "primes found in", endtime - starttime, "seconds.")
