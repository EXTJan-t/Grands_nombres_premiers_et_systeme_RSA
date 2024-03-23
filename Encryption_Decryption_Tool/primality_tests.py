import math, random
import helpers

#Deterministic tests
#Totally accurate however too slow when facing large numbers
def BruteforceEnumeration(n):
    """
    int -> bool
    returns if n is a prime number using brute force
    """
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


#Probabilistic tests
#Generally much faster but not 100% accurate, these tests can mistakenly identify composite numbers as primes, though not the other way around.
def Fermat(n, test_time = 1000):
    """
    int -> bool
    returns if n is a prime number using probalistic tests based on Fermat's little theorem
    2 ** 340 % 341 == 1
    341 = 11 * 31
    """
    if n < 2:
        return False
    for _ in range(test_time):
        a = random.randint(2, 2 ** 16 - 1)
        if helpers.fast_exponentiation_iter(a, n - 1, n) != 1:
            return False
        
    return True

#@https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def Miller_Rabin(n, test_time = 1000):
    """
    int -> bool
    returns if n is a prime number using probalistic tests based on Miller-Rabin primality test
    """
    if n < 3 or n % 2 == 0:
        return n == 2
    
    #n - 1 = 2 ^ s * d
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    for _ in range(test_time):
        a = random.randint(2, n - 2)
        x = helpers.fast_exponentiation_iter(a, d, n)

        for _ in range(s):
            y = helpers.fast_exponentiation_iter(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
        if y != 1:
            return False
    
    return True
