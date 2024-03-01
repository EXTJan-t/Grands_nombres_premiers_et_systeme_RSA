import os

PUBLIC_KEY = "public_key.txt"

def encryption(x):
    """
    int -> int
    Generates a cypher code according to the public key generated
    """
    assert os.path.getsize(PUBLIC_KEY), "Cannot find a public key in the file to continue the process, please generate one"
    with open(PUBLIC_KEY, 'r') as file:
        t = file.readline().split()
        
        N, e = int(t[4]), int(t[5])

        #y = (x ** e) % N
        y = 1
        for i in range(e):
            y *= x
            y %= N

        return y

def textEncryption(s):
    """
    String -> List<int>
    Generates a cypher text according to the public key generated
    """
    t = [chr(encryption(ord(x))) for x in s]
    return "".join(t)

if __name__ == "__main__":
    plain = int(input("What is the number that you wish to encrypt: \n"))
    cypher = encryption(plain)
    print("Your Cypher code is" , cypher)

    plain = input("What is the phrase that you wish to encrypt: \n")
    cypher = textEncryption(plain)
    print("Your Cypher text is" , cypher)
