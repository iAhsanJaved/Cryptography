# Caesar cipher algorithm
def encrypt(plaintext, key):
    """ This fuction will return Ciphertext"""
    ciphertext = ''
    for ch in plaintext:
        if (ch.isupper()):
            # EncryptedChar = (char + key) % 26
            ciphertext += chr((ord(ch) + key - 65)%26 + 65)
        elif (ch.islower()):
            # EncryptedChar = (char + key) % 26
            ciphertext += chr((ord(ch) + key - 97)%26 + 97)
        else:
            ciphertext += ' '
    return ciphertext

def decrypt(ciphertext, key):
    """ This fuction will return plantext"""
    plantext = ''
    for ch in ciphertext:
        if (ch.isupper()):
            # EncryptedChar = (char + key) % 26
            plantext += chr((ord(ch) - key - 65)%26 + 65)
        elif (ch.islower()):
            # EncryptedChar = (char + key) % 26
            plantext += chr((ord(ch) - key - 97)%26 + 97)
        else:
            plantext += ' '
    return plantext

plaintext = input('Enter the planetext: ')
key = int(input('Enter the key (shift): '))

ciphertext = encrypt(plaintext,key)
print('\nCiphertext: ' + ciphertext)
plaintext = decrypt(ciphertext, key)
print('Plaintext: ' + plaintext)