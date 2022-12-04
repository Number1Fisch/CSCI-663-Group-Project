"""

This is the Python script to simulate RSA Encryption

"""

from math import gcd
from egcd import egcd
import random as rand


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True



def computeLambdaN(p, q):
    return int(((p - 1) * (q - 1)) / gcd((p - 1), (q - 1)))

# n = p * q, p and q are large primes

# choose int e, s.t. 1 < e < lambdaN and gcd(e , lambdaN) == 1

def computeCompatibleE(lambdaN):
    compatibleE = []
    for i in range(lambdaN):
        if gcd(i, lambdaN) == 1:
            compatibleE.append(i)
    return compatibleE

def chooseE(lambdaN):
    e = rand.choice(computeCompatibleE(lambdaN))
    return e

# calculates d(ecrypt), the value which you take the encrypted message to the power of

def calculateD(lambdaN, e):
    d = egcd(e, lambdaN)[2] % lambdaN
    return d

#returns encrypted message as list of values

def encryptMessage(message):
    encryptedMessage = []

    for i in range(len(message)):
        encryptedMessage.append(ord(message[i]))
        encryptedMessage[i] = pow(encryptedMessage[i], e, n)
   

    return encryptedMessage

# precondition: encryptedMessage, a list of encrypted char values; d, calculated from calculateD; n, from p * q

def decryptMessage(encryptedMessage, d, n):

    for i in range(len(encryptedMessage)):
        encryptedMessage[i] = pow(encryptedMessage[i], d, n)
        encryptedMessage[i] = chr(encryptedMessage[i])

    return encryptedMessage.join("")
