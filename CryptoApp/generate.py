import string
import random

def generate_address():
    alph=string.ascii_letters+string.digits
    address='T'+ ''.join(random.choices(alph,k=33))
    return address

def generate_uid():
    alph=string.digits
    uid=''.join(random.choices(alph,k=6))
    return uid