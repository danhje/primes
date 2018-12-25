'''
@author: Daniel Hjertholm
'''



def primes(ubound):
    '''
    Brute force algorithm that takes every number up to ubound and tests for
    primality. Tests for primality by trying to divide by every smaller number.
    '''

    primes_list = [2]
    for i in range(3, ubound):
        for o in range(2, i):
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
