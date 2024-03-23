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

    for i in range(2, int(math.sqrt(n)) + 1):
        if math.gcd(n, i) == 1:
            return i
    return

def find_modular_inverse(p, n):
    """
    int x int -> int
    finds a number q such that (pq = 1) mod n 
    """
    p = p % n
    for q in range(1, n):
        if (q * p) % n == 1:
            return q
    
    return



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











