"""

This is the Python script to simulate RSA Encryption

"""

from math import gcd
from egcd import egcd
import random as rand


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

p = 17
q = 29
n = p * q
print(egcd(17,29))
lambdaN = computeLambdaN(p, q)
e = rand.choice(computeCompatibleE(lambdaN))
d = egcd(e, lambdaN)[2] % lambdaN

message = input("message: ")

encryptedMessage = []

for i in range(len(message)):
    encryptedMessage.append(ord(message[i]))
    encryptedMessage[i] = pow(encryptedMessage[i], e, n)
   



print("encrypted message:",encryptedMessage)


for i in range(len(encryptedMessage)):
    encryptedMessage[i] = pow(encryptedMessage[i], d, n)
    encryptedMessage[i] = chr(encryptedMessage[i])

print("message:",message)
