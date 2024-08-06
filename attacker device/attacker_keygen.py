from Crypto.PublicKey import RSA
import Crypto
import os
import sympy
from Crypto.Util import number


created = False
while not created:
    try:
        p = sympy.randprime(pow(2,8), pow(2,24))
        q = sympy.randprime(pow(2,8), pow(2,24))
        n = p*q
        phi_n = (p-1)*(q-1)
        exponent = 65537 
        d = pow(exponent, -1, phi_n)
        print("Your attacker key has been generated and saved in attacker_public.pem [PUBLIC KEY] and attacker_private.pem [PRIVATE KEY]")
        backdoored_key = Crypto.PublicKey.RSA.construct((n , exponent, d,))
        public_attacker = backdoored_key.publickey().export_key()
        private_attacker = backdoored_key.export_key()

        with open("attacker_public.pem", "wb") as f:
            f.write(public_attacker)

        with open("attacker_private.pem", "wb") as f:
            f.write(private_attacker)
        created = True
    except:
        print("Error occured while creating key, trying again")


