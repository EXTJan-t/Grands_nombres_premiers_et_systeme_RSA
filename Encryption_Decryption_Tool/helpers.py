import random
import math
import primality_tests

def is_prime(n):
    return primality_tests.Miller_Rabin(n)

def generate_random_prime(min_val, max_val):
    """
    
    """
    while True:
        num = random.randint(min_val, max_val)
        if is_prime(num):
            return num

def input_generator(min_val, max_val):
    """
    int -> Tuple<int>
    asks the user for a prime number of d digits 
    """
    res = int(input("Please provide a prime number between" + min_val + max_val))
    while not res.isnumeric() or min_val <= res < max_val: 
        res = int(input("Please provide a prime number between" + min_val + max_val))
    
    return res

def generate_prime_number(min_val, max_val):
    """
    int -> Tuple<int>
    Generates a prime number between min_val and max_val.
    """
    return generate_random_prime(min_val, max_val)


#-------------------------------------------------------------------------------------------------------


def find_coprime(n):
    """
    int -> int
    returns a number that is coprime with n
    """
    assert n != 1, "There's no coprime for 1"

    while True:
        i = random.randint(2, n - 2)
        if math.gcd(n, i) == 1:
            return i
    

def extended_euclidean(a, b):
    """
    int X int -> int X int X int
    returns gcd(a, b), x, y, such that ax + by = gcd(a, b)
    """
    if a == 0:
        return b, 0, 1
    
    g, x, y = extended_euclidean(b % a, a)
    return (g, y - (b // a) * x, x)

def find_modular_inverse(p, n):
    """
    int x int -> int
    finds a number q such that (pq = 1) mod n using extended euclidiean algorithm
    """
    g, x, y = extended_euclidean(p, n)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % n


#---------------------------------------------------------------------------------------------------
#Exponentiations
def fast_exponentiation_recur(a, n, MOD = 1):
    """
    int X int -> int
    Calculates a ** n % MOD using fast exponentiation algorithm
    Recursive version
    """
    if n == 0:
        return 1
    
    if n == 1:
        return a % MOD
    
    if n % 2 == 0:
        b = fast_exponentiation_recur(a, n // 2, MOD)
        return b * b % MOD
    else:
        b = fast_exponentiation_recur(a, (n - 1) // 2, MOD)
        return (b * b) * a % MOD
    
def fast_exponentiation_iter(a, n, MOD = 1):
    """
    int X int -> int
    Calculates a ** n % MOD using fast exponentiation algorithm
    Iterative version
    """
    res = 1
    i = 0
    while (n >> i) != 0:
        if (n >> i) & 1:
            res *= a
            res %= MOD
        a *= a
        a %= MOD

        i += 1
        
    return res

#----------------------------------------------------------------------------------------------------------------------






