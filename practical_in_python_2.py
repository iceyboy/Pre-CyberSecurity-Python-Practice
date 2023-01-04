import math

yourName = "Claire Marie"
print(yourName)
print(len(yourName))
print(yourName[:2])
print(yourName.upper())
print(yourName.replace('a', '#'))
print("The character 'a' first occurs in position " + str(yourName.find('a')))
print("The character 'a' first occurs in position " + str(yourName.rfind('a')))

side = int(input("what is the side length"))
area = side * side
print(area)

radius = int(input("what is the radius"))
area = math.pi * radius * radius 
print("{:.2f}".format(area))

userNumber = float(input("enter a decimal number in the format xx.xxxx eg 12.3456"))
rounded = "{:.2f}".format(userNumber)
squared = "{:.3f}".format(userNumber*userNumber)
cubed = "{:.3f}".format(userNumber*userNumber*userNumber)
squareRoot = "{:.4f}".format(math.sqrt(userNumber))
print(userNumber)
print(rounded)
print(squared)
print(cubed)
print(squareRoot)






