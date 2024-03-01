from helpers import *

#The larger the primes used to generate the keys, the safer the encryption
PRIME_DIGITS = 0

def generate_keys(prime_generator = generate_prime_number):
    """
    int X func -> Tuple<Tuple<int>>
    generates our keys for the RSA encryption such as:
    (public key, private key) 
    where two keys are such that: (a, b)
    """
    p, q = prime_generator(1, 1000), prime_generator(1, 1000)

    N = p * q

    #phi(n) = n - 1 for any n prime
    #phi(ab) = phi(a) x phi(b) for a, b prime
    phi_N = (p - 1) * (q - 1)

    e = find_coprime(phi_N)

    d = find_modular_inverse(e, phi_N)

    public_key = (N, e)
    private_key = (N, d)

    return public_key, private_key


def change_keys():
    public_key, private_key = generate_keys()
    print("Your public key is:", public_key)
    print("Your private key is:", private_key)

    with open("public_key.txt", 'w') as file1, open("private_key.txt", 'w') as file2:
        file1.write("Your public key is: " + str(public_key[0]) + " " + str(public_key[1]))
        file2.write("Your private key is: " + str(private_key[0]) + " " + str(private_key[1]))

if __name__ == "__main__":
    change_keys()





