"""
ECDSA signing example from: https://pypi.org/project/ecdsa/
"""

from ecdsa.util import PRNG #default is to use system urandom
from ecdsa import SigningKey, NIST384p #import curve to use, default is NIST192p (does not have to be imported)

import hashlib #default uses sha1

rng1 = PRNG("seed_to_start") 
print("\n\n\n******Warning******\nThis example uses a set seed. Using the same random number twice to generate keys will reveal private keys!\n")

sk = SigningKey.generate(curve = NIST384p, entropy = rng1) # longer keys with higher NISTps
vk = sk.get_verifying_key()
vk_string = vk.to_string() #not needed, just for kicks

msg = "This was the first coding challenge at Insight DC SV19"
msgEncoded = msg.encode('utf-8')

#sign the message
signature = sk.sign(msgEncoded, hashfunc=hashlib.sha256)

conf = vk.verify(signature, msgEncoded, hashfunc=hashlib.sha256)

print('\n******Message******\n' + msg) 
print('\n\n******Verifying key******\n' + str(vk_string))
print('\n******Confirmation******\nVerification status of signature is ' + str(conf)+'\n\n') 