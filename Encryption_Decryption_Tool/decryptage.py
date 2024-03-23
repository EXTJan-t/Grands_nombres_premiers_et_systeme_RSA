import os
import helpers

PRIVATE_KEY = "private_key.txt"

def decryption(y):
    """
    int -> int
    Generates a cypher code according to the public key generated
    """
    assert os.path.getsize(PRIVATE_KEY), "Cannot find a private key in the file to continue the process, Please generate one"
    with open(PRIVATE_KEY, 'r') as file:
        t = file.readline().split()

        N, d = int(t[4]), int(t[5])

        #x = (y ** d) % N
        x = 1
        for _ in range(d):
            x *= y
            x %= N

    return helpers.fast_exponentiation_iter(y, d, N)

def textDecryption(s):
    """
    String -> List<int>
    Generates a cypher text according to the public key generated
    """
    t = [chr(decryption(ord(x))) for x in s]
    return "".join(t)

if __name__ == "__main__":
    cypher = int(input("What is the number that you wish to decrypt: \n"))
    plain = decryption(cypher)
    print("Your Plain code is" , plain)

    cypher = input("What is the phrase that you wish to decrypt: \n")
    plain = textDecryption(cypher)
    print("Your Plain text is" , plain)
