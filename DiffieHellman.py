"""

This is the Python Script to simulate a Diffie-Hellman Key Exchange

"""
import sys
#
def computePublic(alpha, p, privateKey):
    if privateKey >= p:
        sys.exit("Secretly chosen number must be smaller than p, " + str(p) + ".")
    return (alpha ** privateKey) % p


def computeSecret(alpha, p, publicKey):
    return (alpha ** publicKey) % p

def diffieHellmanKeyExchange(alpha, p, alicePrivate, bobPrivate):

    # computations of public keys, from secretly chosen alicePrivate and bobPrivate
    alicePublic = computePublic(alpha, p, alicePrivate)
    bobPublic = computePublic(alpha, p, bobPrivate)


    ################################################
    # public transfer of alicePublic and bobPublic #
    ################################################

    # Alice computing s
    aliceS = computeSecret(alpha, p, bobPublic)

    # Bob computing s
    bobS = computeSecret(alpha, p, alicePublic)


    # Should return true
    return bobS == aliceS
    
    
# need a function to determine alpha from p
