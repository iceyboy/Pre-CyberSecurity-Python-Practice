#B- Substitution Cipher 
#The substitution cipher is a cryptosystem which offers resistance to brute force attacks due 
#to its huge key space. The key in this cipher is a table that matches the plaintext letters to 
#the corresponding ciphertext ones. The encryption and decryption are checking the look-up 
#table in one way or the other. 
#1. Define a substitution key 
#2. Implement substitution_encrypt() and substitution_decrypt() for encryption and 
#decryption using the substitution cipher 
#Note that the index() method can be used on a string to give the index of a character 
#within a string. 

alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "fcpevqkzgmtrayonujdlwhbxsi"

def substitution_encrypt(text):

    result = ""

    for letter in text:

        if letter.lower() in alphabet:

            result += key[alphabet.find(letter.lower())]

        else:

            result += letter

    print(result)

def substitution_decrypt(text):

    result = ""

    for letter in text:

        if letter.lower() in key:

            result += alphabet[key.find(letter.lower())]

        else:

            result += letter

    print(result)



substitution_encrypt("hello")
substitution_decrypt("zvrro")