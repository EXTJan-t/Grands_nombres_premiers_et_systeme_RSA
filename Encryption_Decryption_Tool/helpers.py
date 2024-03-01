import random
from math import gcd, sqrt

def is_prime(n):
    """
    int -> bool
    checks if a number is a prime
    (can be slow for very large numbers)
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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

    for i in range(2, int(sqrt(n)) + 1):
        if gcd(n, i) == 1:
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








