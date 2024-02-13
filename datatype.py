# Datatype
number = 60  # int
num = 34.78  # float
greeting = "Hello there"  # str
is_Python_Interesing = True  # bool

# A variable with multiple values
languages = ["python", "php", "java", "kotlin"]  # List
fruits = ("apple", "banana", "pineapple")  # Tuple
countries = {"Kenya", "Ghana", "Italy", "China"}
# Dictionary
details = {
    "firstname": "Ashley",
    "course": "MIT",
    "age": "18",
    "nationality": "USA"
}

print(number)
print(num)
print(greeting)
print(is_Python_Interesing)
print(countries)
print(details)
print(details["firstname"])
print(details["nationality"])

# Fetermining the data type of a variable
print(type(details))
print(type(countries))
print(type(greeting))

# Typecasting - Converting one data  type to another
print(float(number))
print(int(num))

