import sympy
from Crypto.PublicKey import RSA
import Crypto
import os
import math

def split_in_binary(bin):
    bin = "{0:b}".format(bin)
    bin = "0"*(48*2-len(bin)) + bin
    pre = bin[:len(bin)//2]
    post = bin[len(bin)//2:]
    return(int(pre , 2), int(post , 2))

f = open("attacker_private.pem" , "r")
private_key = f.read()
f.close()

attacker_private = RSA.import_key(private_key)

f = open("attacker_public.pem" , "r")
public_key = f.read()
f.close()

attacker_public = RSA.import_key(public_key)

f = open("victim_public.pem" , "r")
public_key = f.read()
f.close()

victim_public = RSA.import_key(public_key)


def calc_secrets(vp):

    p = pow(vp, attacker_private.d, attacker_public.n)
    q =  int(victim_public.n//p)
    phi_n =  int((p-1)*(q-1))
    
    try:
        D = pow(victim_public.e , - 1 ,phi_n)
        print(D)
        return D
    except ValueError:
        print("Error calculating private key ...")

collection_user = {}

collection_user["vp"] = split_in_binary(victim_public.n)[0]
collection_user["vp_2"] = collection_user["vp"]+1

try:
    secrets_one = calc_secrets(collection_user["vp"])
    victim_private_key = Crypto.PublicKey.RSA.construct((victim_public.n , victim_public.e, secrets_one,)).export_key()
    print("FOUND PRIVATE KEY. Saved to cracked.pem")
    with open("cracked.pem", "wb") as f:
        f.write(victim_private_key)
except:
    try:
        secrets_two = calc_secrets(collection_user["vp_2"])
        victim_private_key = Crypto.PublicKey.RSA.construct((victim_public.n , victim_public.e, secrets_two,)).export_key()
        print("FOUND PRIVATE KEY. Saved to cracked.pem")
        with open("cracked.pem", "wb") as f:
            f.write(victim_private_key)
    except:
        print("Cant derieve private key")

