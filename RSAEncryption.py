"""

This is the Python script to simulate RSA Encryption

"""

from math import gcd
from egcd import egcd
import random as rand
class RSA():
    # variables for encryption values
    n = 0
    e = 0
    d = 0
    plainText = ""
    cipherText = ""
    def encrypt():

        for i in range(len(plainText)):
            cipherText.append(ord(plainText[i]))
            cipherText[i] = pow(cipherText[i], e, n)

    def decrypt(cipherText):
        for i in range(len(encryptedMessage)):
            encryptedMessage[i] = pow(encryptedMessage[i], d, n)
            encryptedMessage[i] = chr(encryptedMessage[i])
            return encryptedMessage

def primeCheck(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True



def computeLambdaN(p, q):
    return int(((p - 1) * (q - 1)) / gcd((p - 1), (q - 1)))

def computeCompatibleE(lambdaN):
    compatibleE = []
    for i in range(lambdaN):
        if gcd(i, lambdaN) == 1:
            compatibleE.append(i)
    return compatibleE
# n = p * q, p and q are large primes

# lambdaN = computeLambdaN(p, q)

# choose int e, s.t. 1 < e < lambdaN and gcd(e , lambdaN) == 1
