temperature = 32
if temperature > 37:
    print("It is hot")

else:
    print("It is cold")

# A programme that prints the largest among three numbers
num1 = 45
num2 = 89
num3 = 32
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 >num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")
# A program that checks whether a number is odd or even
number = 58
if number % 2 ==0:
    print(number,"is even")
else:
    print(number,"is odd")
n = 7
if n>1:
    for i in range(2,n//2):
        if(n%i)==0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
else:
        print(n, "is neither prime nor composite")




