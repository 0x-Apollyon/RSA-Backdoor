import sympy
import math
from Crypto.Util import number
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import Crypto
import os
import time

def concatenate_in_binary(pre, post):
    pre = "{0:b}".format(pre)
    post = "{0:b}".format(post)

    pre = "0"*(48-len(pre)) + pre
    post = "0"*(48-len(post)) + post

    return int((pre + post),2)

f = open("attacker_public.pem" , "r")
public_key = f.read()
f.close()


attacker_public = RSA.import_key(public_key)

valid = False
while not valid:
    p = sympy.randprime(pow(2,16), pow(2,48))
    vP = pow(p, attacker_public.e ,attacker_public.n)

    lower_bound_q = math.ceil(concatenate_in_binary((vP-1), 0)/p)
    upper_bound_q = math.floor(concatenate_in_binary(vP, (pow(2, 48)-2))/p)

    try:
        q = int(sympy.randprime(lower_bound_q , upper_bound_q ))
        valid = True
        
    except ValueError:
        print("Margin too small")
        pass

created = False
while not created:
    try:
        phi_n = (p-1)*(q-1)
        exponent = 65537
        d = pow(exponent, -1 , phi_n)
        n = p*q

        created = True
        backdoored_key = Crypto.PublicKey.RSA.construct((n , exponent, d,))

        public_backdoored = backdoored_key.publickey().export_key()
        private_backdoored = backdoored_key.export_key()

        with open("victim_public.pem", "wb") as f:
            f.write(public_backdoored)

        with open("victim_private.pem", "wb") as f:
            f.write(private_backdoored)

        print("The backdoored victims key has been saved to victim_public.pem [PUBLIC KEY] and victim_private.pem [PRIVATE KEY]")
        print((n , exponent, d,))
    except:
        print("Error while generating key. Retrying ...")
        pass



