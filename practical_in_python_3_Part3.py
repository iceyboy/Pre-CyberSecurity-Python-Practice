age = int(input("Please enter your age : "))

if age < 1:
    print("Sorry don't recognise your input")
    exit()

if age > 17:
    name = input("Please enter your name: ")

    print("Age: " + str(age) + "\n" + "Name: " + name)

else:
    print("Too young to continue")