

def caesar_cipher(plaintext):

    ciphertext = ''

    for letter in plaintext:

        if letter.isupper():

            cod = ord(letter)
            cod = cod + 10

            if cod <= ord('Z'):

                ciphertext = ciphertext + chr(cod)

            elif cod > ord('Z'):

                ciphertext = ciphertext + chr(cod - 26)


        elif letter.islower():

            cod = ord(letter)
            cod = cod + 10

            if cod <= ord('z'):

                ciphertext = ciphertext + chr(cod)

            elif cod > ord('z'):

                ciphertext = ciphertext + chr(cod - 26)


        else:

            ciphertext = ciphertext + letter


    cipher = 'Gtrsed'

    results = [ciphertext, cipher]

    return results