#ASCII
"""
print("Program Started!")
print("Please enter a standard character:")

letter = input()

if len(letter) == 1:
    value = ord(letter)
    print(f"The ASCII code for {letter} is {value}.")
else:
    print("Error: Please enter exactly one character.")

print("Program Ended!")

"""


#TASK2
"""
print("Program Started!")
print("Please enter an ASCII code:")

code = abs(int(input()))

if code in range(32, 127):
    character = chr(code)
    print(f"The character represented by the ASCII code {code} is {character}.")
else:
    print("Error: The ASCII code must be between 32 and 126 inclusive.")

print("Program Ended!")

"""

#TASK3
"""
# The function
def greet_user():
    print("Please enter your name")
    name = input()
    print("Hello", name)

# Call to function
greet_user()

"""

"""
#TASK4

# The function
def sum():
    print("Please enter 2 numbers")
    number1 = int(input())
    number2 = int(input())
    result = number1 +number2
    print(result)

# Call to function
sum()

"""

#TASK5
"""
# The function
def sum(number1,number2):
    result = number1 +number2
    print(result)

# Call to function
sum(50, 40)

"""

"""
#TASK5
def escape_by(plan):

    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")

    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")

    elif plan == "cross bridge ahead":
        print("We cannot escape that way! The boulder is in the way!")
        
    else:
        print("We cannot escape that way! The boulder is in the way!")
#call function
escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")

"""

#TASK6
"""
#function to cross the bridge

def cross_bridge(distance):

    #repeat for each step crossed
    for step in range(distance):
        print("Crossed step.")

    #check if the brigde is too logn
    if distance > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep gooing!")

#call the fuction

cross_bridge(3)
cross_bridge(6)

"""
"""
#TASK7

def addition(x, y):
    return x + y

# Calling the function
result = addition(10, 20)
print(result)

"""
"""
#TASK8

def display_box(name):
    message = f"* Hello {name} *"
    print("*" * len(message))
    print(message)
    print("*" * len(message))

def greet_user():
    print("Please enter your name")
    name = input()
    display_box(name)

greet_user()
"""
#TASK9
"""
def get_name():
    print("Please enter your name")
    name = input()
    return name

print("Retrieved name:", get_name())
 
 """
"""
 #TASK10


# Function 1: Calculate total weight
def sum_weights(person, inventory):
    return person + inventory


# Function 2: Calculate average weight
def calc_avg_weight(person, inventory):
    total = sum_weights(person, inventory)
    return total / 2


# Function 3: Run the program
def run():
    person = float(input("What is the weight of the person?\n"))
    inventory = float(input("What is the weight of their inventory?\n"))

    choice = input("What would you like to calculate (sum or average)?\n")

    if choice == "sum":
        print("The sum of weights is", sum_weights(person, inventory))

    elif choice == "average":
        print("The average weight is", calc_avg_weight(person, inventory))


# Run the program
run()
"""

import random as rnd

print(rnd.randrange(0, 100, 15))