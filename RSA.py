import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

# def modpow(a,b,m):
#     result = 1
#     while (b > 0):
#         if (b & 1):
#             result = (result * a) % m
#         a = (a * a) % m
#         b >>= 1
#     return result

def encrypt(m, e, n):
    c = [pow(ord(char), e, n) for char in m]
    # c = pow(m,e,n)
    return c

def decrypt(c, d, n):
    # d = pow(c,d,n)
    d = "".join([chr(pow(i, d, n)) for i in c])
    return d;
    

def keygen(p, q):
    phi = (p-1)*(q-1)
    n = p*q
    e_values = []
    for i in range(2, phi):
        if gcd(i, phi) == 1:
            e_values.append(i)
    e = e_values[random.randrange(1, len(e_values))]
    d = multiplicative_inverse(e,phi)
    return ((e,n),(d,n))


def main():
    p = int(input(" - Enter a prime number (17, 19, 23, etc): "))
    q = int(input(" - Enter another prime number (Not one you entered above): "))
    if(not is_prime(p) or not is_prime(q)):
        raise ValueError("Both of them should be prime")
    elif p == q:
        raise ValueError('p and q cannot be equal')
    
    n = p*q;
    public, private = keygen(p,q)
    print("Public Key:", public)
    print("Private Key:", private)

    m = (input("Enter the message to be encrypted and decrypted"))
    c = encrypt(m,public[0],n)
    dec = decrypt(c,private[0],n)
    print("Encrypted:", c)
    print("Decrypted:", dec)

main()