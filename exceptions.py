# exceptions = Errors

try:
    print(x)
except:
    print("An error occured")
finally:
    print("Success")
num1 = 20
num2 = 0

try:
    print(num1 / num2)
except:
    print("zeroDivisionError occured")

# User-defined functions
try:
    def multiply(number1, number2):
        print(number1 * number2)
except:
    print("An error occured")
finally:("Success")
multiply(6, 5)