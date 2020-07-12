'''
@author: Daniel Hjertholm
'''


import math
from typing import List, Optional


def primes1(ubound: int) -> List[int]:
    '''
    Brute force algorithm that takes every number up to ubound and tests for
    primality. Tests for primality by trying to divide by every smaller number.

    Example:

    >>> primes1(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    '''

    primes_list = [2]
    for i in range(3, ubound):
        for o in range(2, i):
            if i % o == 0:
                break
        else:
            primes_list.append(i)
    return primes_list


def primes2(ubound: int) -> List[int]:
    '''
    This algorithm takes every odd number up to ubound and tests for primality.
    Tests for primality by trying to divide by every smaller number.

    Example:

    >>> primes2(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    '''

    primes_list = [2]
    for i in range(3, ubound, 2):
        for o in range(2, i):
            if i % o == 0:
                break
        else:
            primes_list.append(i)
    return primes_list


def primes3(ubound: int) -> List[int]:
    '''
    Takes every odd number up to ubound and tests for primality. Tests for
    primality by checking the remainder after dividing with the primes already
    found.

    Example:

    >>> primes3(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    '''

    primes_list = [2]
    for i in range(3, ubound, 2):
        for o in primes_list:
            if i % o == 0:
                break
        else:
            primes_list.append(i)
    return primes_list


def primes4(ubound: int) -> List[int]:
    '''
    Starts with list of ints up to ubound, and uses map to "None out" those
    that are not primes. Tests for primality by dividing by ints up to the
    number being tested and checking if the remainder is 0.

    Example:

    >>> primes4(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    '''

    def is_prime(num: int) -> Optional[int]:
        for o in range(2, num):
            if num % o == 0:
                return None
        else:
            return num

    primes_list = [2] + list(map(is_prime, range(3, ubound, 2)))
    for i in range(primes_list.count(None)):
        primes_list.remove(None)
    return primes_list


def primes5(ubound: int) -> List[int]:
    '''
    Starts with list of ints up to ubound, and uses map to "None out" those
    that are not primes. Tests for primality by dividing by ints up to the
    square root of the number being tested and checking if the remainder is 0.

    Example:

    >>> primes5(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    '''

    def is_prime(num: int) -> Optional[int]:
        for o in range(2, int(math.ceil(math.sqrt(num))) + 1):
            if num % o == 0:
                return None
        else:
            return num

    primes_list = [2] + list(map(is_prime, range(3, ubound, 2)))
    for i in range(primes_list.count(None)):
        primes_list.remove(None)
    return primes_list


def primes6(ubound: int) -> List[int]:
    '''
    Takes every odd number up to ubound and tests for primality. Tests for
    primality by checking the remainder after dividing with the primes already
    found that are smaller than the square root of the number being checked.

    Example:

    >>> primes6(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    '''
    primes_list = [2]
    for i in range(3, ubound, 2):
        primes_list_sub = [elem for elem in primes_list if elem <= math.sqrt(i)]
        for o in primes_list_sub:
            if i % o == 0:
                break
        else:
            primes_list.append(i)
    return primes_list


def primes7(ubound: int) -> List[int]:
    '''
    Starts with list of odd ints up to ubound, and uses filter to keep only
    those that are primes. Tests for primality by dividing by ints up to the
    square root of number being tested and checking if the remainder is 0.

    Example:

    >>> primes7(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    '''

    def is_prime(num: int) -> bool:
        for o in range(2, int(math.ceil(math.sqrt(num))) + 1):
            if num % o == 0:
                return False
        else:
            return True

    x = range(3, ubound, 2)
    return [2] + list(filter(is_prime, x))


def primes8(ubound: int) -> List[int]:
    '''
    Starts with range of odd ints up to ubound, and uses filter to keep only
    those that are primes. Tests for primality using the 6k +/- 1 optimization.

    Example:

    >>> primes8(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    '''

    def is_prime(num: int) -> bool:
        if num <= 3:
            return num > 1
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    x = range(3, ubound, 2)
    return [2] + list(filter(is_prime, x))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
