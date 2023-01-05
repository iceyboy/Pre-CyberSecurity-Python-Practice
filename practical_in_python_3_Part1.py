finalMark = int(input("Enter mark ..."))

if finalMark >= 70 and finalMark <= 100:
    print("Classification : Distinction")
elif finalMark >= 60 and finalMark <= 69:
    print("Classification : Merit")
elif finalMark >= 50 and finalMark <= 59:
    print("Classification : Pass")
elif finalMark >= 0 and finalMark <= 49:
    print("Classification : Fail")
else:
    print("User input outside of suitable range")
    