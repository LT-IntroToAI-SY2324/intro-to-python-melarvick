# Complete your individualized AI problems here

# def fizbuzz(input_num):
#     if(input_num%3==0):
#         if(input_num%5==0):
#             return 'FizzBuzz'
#         return 'Fizz'
#     elif(input_num%5==0):
#         return 'Buzz'
#     else:
#         return input_num

# assert fizbuzz(1) == 1, "fizzbuzz 1 test"
# assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
# assert fizbuzz(4) == 4, "fizzbuzz 4 test"
# assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
# assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
# assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"


# Problem 1: Hello, World!
# Write a Python program that prints "Hello, World!" to the console.

print("Hello, World!")

# Problem 2: Variables and Data Types
# Declare variables in Python and print their values.

name= "Morgan"
age= 16
height= 5.75
is_student= True

print(name)
print(age)
print(height)
print(is_student)

# Problem 3: User Input
# Write a program that takes the user's name as input and greets them.

name= input("What is your name?")
print("Hello," + input)

# Problem 4: Conditional Statements
# Write a Python program that checks if a number is positive, negative, or zero.

number= float(input("Enter a number: "))

if number>0:
    print("Positive")
elif number<0:
    print("Negative")
else:
    print("Zero")

# Problem 5: Loops
# Write a Python program that prints the numbers from 1 to 10 using a for loop.

for num in range(1,11):
    print(num)

# Problem 6: Functions
# Write a Python function to calculate the factorial of a given number.

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

result = factorial(5)
print("factorial of 5:", result)

# Problem 7: Lists
# Create a Python list of fruits and print each fruit using a for loop.

fruits=["apple", "banana", "pear", "grapes", "strawberry"]
for elem in fruits:
    print(fruits)

# Problem 8: Dictionaries
# Create a Python dictionary to store the names and ages of people. Print out the ages of each person.

people = {
    "Morgan": 16,
    "Bob": 30,
    "Charlie": 22
}

for name, age in people.items():
    print(name + " is " + str(age) + " years old.")
