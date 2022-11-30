"""

This is the Python Script to simulate a Diffie-Hellman Key Exchange

"""
import sys
import random as rand
#
def computePublic(alpha, p, privateKey):
    if privateKey > p - 1 or privateKey < 2:
        sys.exit("Secretly chosen number must be between 2 and p - 1, " + str(p) + ".")
    return pow(alpha, privateKey, p - 1)


def computeSecret(alpha, p, publicKey):
    return pow(alpha, publicKey, p - 1)

def diffieHellmanKeyExchange(p, alicePrivate, bobPrivate):

    alpha = primitiveElement(p)
    if (alpha == []):
        sys.exit("p " + str(p) + " not suitable for exchange")
    alpha = rand.choice(alpha)

    print("What Oscar sees:")

    print("Alpha is " + str(alpha))

    # computations of public keys, from secretly chosen alicePrivate and bobPrivate
    print("Alice and Bob are computing public keys")

    alicePublic = computePublic(alpha, p, alicePrivate)
    bobPublic = computePublic(alpha, p, bobPrivate)
    
    print("Public keys are", alicePublic, "and", bobPublic)
    ################################################
    # public transfer of alicePublic and bobPublic #
    ################################################

    # Alice computing s
    aliceS = computeSecret(alpha, p, bobPublic)

    # Bob computing s
    bobS = computeSecret(alpha, p, alicePublic)

    if bobS == aliceS:
        print("The secret Keys have been exchanged")
    
    
# function to determine possible alpha from p, alpha must be a primitive element

def primitiveElement(p):
    elementsList = []
    for i in range(p):
        count = 1 # to determine order of ring
        oldI = i # element to multiply repeatedly
        i = i * oldI
        while(i != oldI and i != 0):
            i = (i * oldI) % p
            count += 1
            if count >= p:
                break

        if count == p - 1: # case where i is cyclic in GF(p) of order p-1
            elementsList.append(i) # add to possible alpha value list

    return elementsList

print("Determine Input Parameters")
inputp = int(input("p: "))
inputa = int(input("Alice's Private Key: "))
inputb = int(input("Bob's Private Key: "))
print()

diffieHellmanKeyExchange(inputp, inputa, inputb)
#diffieHellmanKeyExchange(97, 31, 54)
