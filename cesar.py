"""
Consulta chatgpt: Code in python for cesar encryption that can 
accept 2 parameters, first string to encrypt and second int with
offset value and I can execute this program in terminal and return
only cypher string
"""

import sys

def encrypt_caesar(text, offset):
    """
    Encrypts the given text using the Caesar Cipher with the given offset.
    """
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + offset - 65) % 26 + 65)
            else:
                result += chr((ord(char) + offset - 97) % 26 + 97)
        else:
            result += char
    return result

if __name__ == '__main__':
    # Read input arguments from the command line
    text = sys.argv[1]
    offset = int(sys.argv[2])

    # Encrypt the text using the Caesar Cipher with the given offset
    cypher = encrypt_caesar(text, offset)

    # Print the resulting cypher string
    print(cypher)