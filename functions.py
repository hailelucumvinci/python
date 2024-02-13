# Inbuilt functions
y = max(67, 56, 43, 89, 23, 4, 78)
print(y)
x = min(12, 4, 67, 89, 34, 2, 78, 76)
print(x)

z = pow(2, 3)
print(z)


# User-defined functions
def details():
    print("Vincent")


details()  # Calling a function


# Parameters and argument
def students(name, course, age):
    print(name, course, age)


students("Ashley", "MIT", 17)
students("Gorrety", "Cybersecurity", 18)


def employees(fullname, Idno, salary, position, Age):
    print(fullname, Idno, salary, position, Age)


employees("Jack Willington", 23456732, 27000, "Sales Person",24 )
employees("Rirrah Shwansei", 23434738, 30000, "Guides person",43 )
employees("Andrew Barrington", 13638387, 64000, "Treasury",34 )
employees("Sheila Jufydma",   34536378, 67000, "Secretary",29)
employees("Dmitritch Ivon", 24638360, 82000, "Managing Director",39)
employees("Vincent Parker", 18938393, 100000, "CEO",47 )
