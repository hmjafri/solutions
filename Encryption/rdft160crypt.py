"""
rdft160crypt.py
"""
"""
Substituion Cipher
"""
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
rot13 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

sub_lookup = {}
rev_lookup = {}
for letter, rot in zip(letters, rot13):
    sub_lookup[letter] = rot
    rev_lookup[rot] = letter

def sub_encrypt(msg):
    """
    Substitution cipher encryption function
    """
    result = ""
    for c in msg:
        if c in sub_lookup:
            result += sub_lookup[c]
        else:
            result += c

    return result


def sub_decrypt(msg):
    """
    Substitution cipher decryption function
    """
    result = ""
    for c in msg:
        if c in rev_lookup:
            result += rev_lookup[c]
        else:
            result += c

    return result

"""
Ceaser Cipher
"""

def ceaser_encrypt(msg, shift_len):
    """
    Ceaser cipher encryption function
    """
  
    result = ""  # For final encrypted msg

    for c in msg:
        if not c.isalpha(): # Only encrypting letters
            result += c
            continue
        
        new = ord(c) + shift_len
        
        if c.islower():
            if new < ord('a'):
                result += chr(ord('z') - (ord('a') - new) + 1)
            elif new > ord('z'):
                result += chr(new - ord('z') + ord('a') - 1)
            else:
                result += chr(new)
        else: #Upper case
            if new < ord('A'):
                result += chr(ord('Z') - (ord('A') - new) + 1)
            elif new > ord('Z'):
                result += chr(new - ord('z') + ord('a') - 1)
            else:
                result += chr(new)
            
    return result
        
def ceaser_decrypt(msg, shift_len):
    """
    Ceaser cipher decryption function
    """
    return ceaser_encrypt(msg, -shift_len)

"""
Block Cipher
"""

def xor(msg, key):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(msg,key))

def block_encrypt(msg, key):
    """
    block cipher encryption function
    """
    result = ""
    block = ""
    for c in msg:
        block += c
        if len(block) < len(key):
            continue

        result += xor(block, key)
        block = ""        
    
    if block:
        result += xor(block, key)
        
    return result


def block_decrypt(msg, key):
    """
    Ceaser cipher decryption function
    """
    return block_encrypt(msg, key)
