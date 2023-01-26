def brute_force(ciphertext):
    letters = "abcdefghijklmnopqrstuvwxyz"
    x = 0

    while x < 26:
        x = x + 1

        ciphertext=ciphertext.lower()

        ciphershift=int(x)

        stringdecrypted=""

        for character in ciphertext:

            position = letters.find(character)

            newposition = position-ciphershift

            if character in letters:

                stringdecrypted = stringdecrypted + letters[newposition]

            else:

                stringdecrypted = stringdecrypted + character
          
          
        ciphershift=str(ciphershift)

        print("Shift of "+ciphershift)
        print("Decrypted message:")
        print(stringdecrypted)
        print("\n")


brute_force("nqtajdtzftnkj")