"""

This is the Python script to simulate RSA Encryption

"""


def gcd(a, b):
    # euclid's algorithm to return greatest common divisor

def primeCheck(num):
    # check for primality, return as boolean



def computeLambdaN(p, q):
    return ((p - 1) * (q - 1)) / gcd((p - 1), (q - 1))

# n = p * q, p and q are large primes

# lambdaN = computeLambdaN(p, q)

# choose int e, s.t. 1 < e < lambdaN and gcd(e , lambdaN) == 1
