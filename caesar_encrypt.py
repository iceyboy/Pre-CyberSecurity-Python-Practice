
def get_letter(num):
    return chr(num + ord('a'))
         


def get_word(num_list):
    
    letter_list = []

    for num in num_list:
        letter_list.append(get_letter(num))

    word = ''.join(letter_list)

    return(word)


def word_to_int(s):
    ranks = []
    for ch in s:
        if ch.isalpha():
            rank = ord(ch.lower()) - ord('a')
            ranks.append(rank)
    return ranks


def letter_to_int(ch):
    return ord(ch.lower()) - ord('a')

def caesar_cipher_encrypt(plaintext, key):

    # empty cipher ranks list 
    c_ranks = []

   # Transform letters to numbers in ℤ26 
    p_ranks= word_to_int(plaintext)

    # encrypt 
    for num in p_ranks:
        c_ranks.append((num + key) % 26)

    # Transform ciphertext back to letters  
    ciphertext = get_word(c_ranks)

    cipherword = ''.join(ciphertext)

     
    print(ciphertext)
    return 0


caesar_cipher_encrypt("bonjour",1)
