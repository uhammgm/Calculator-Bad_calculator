from all_math.meth import *
from all_math.bad_meth import *

pi = 3.14
print("To do \"Bad Math\" add a \".\" to the end of the sign.")
num1 = int(input("First number "))
thing = input("Sign of what you doing ")
num2 = int(input("Second number "))

if thing == "+":
    print(add(num1, num2))

elif thing == "-":
    print(subtract(num1, num2))

elif thing == "/":
    print(divide(num1, num2))

elif thing == "*":
    print(multiply(num1, num2))
elif thing == "+.":
    print(badadd(num1, num2))

elif thing == "-.":
    print(badsubtract(num1, num2))

elif thing == "/.":
    print(baddivide(num1, num2))

elif thing == "*.":
    print(badmultiply(num1, num2))
else:
    print("error")
