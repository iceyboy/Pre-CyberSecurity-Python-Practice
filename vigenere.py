#2. Implement a function encrypt_vigenere(plaintext, keystream) 
# which takes a plaintext and a list of shift values (keystream)
#  and encrypts the plaintext with Vigenère Cipher. 
# You can reuse the functions of the first practical.

def rank_in_block(plaintext, block_len):
    index = 0
    

    for x in plaintext:
        print(x + " is at position " + str(index))
        index += 1
        if index == block_len:
            index = 0


def vigenere(key, message):
    message = message.lower()
    message = message.replace(' ','')
    m = len(key)
    cipher_text = ''
    for i in range(len(message)):
        letter = message[i]
        k= key[i % m] 
        cipher_text = cipher_text + chr ((ord(letter) - 97 + k ) % 26 + 97)

    return cipher_text


def decrypt(key, message):
    message = message.lower()
    message = message.replace(' ','')
    m = len(key)
    cipher_text = ''
    for i in range(len(message)):
        letter = message[i]
        k= key[i % m] 
        cipher_text = cipher_text + chr ((ord(letter) - 97 - k ) % 26 + 97)

    return cipher_text



print(vigenere([1,2,3,4], "hello"))

print(decrypt( [1,2,3,4], "igopp" ))

