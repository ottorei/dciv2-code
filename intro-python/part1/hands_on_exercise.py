"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print("Type: {}, value: {}".format(type(pi), pi))

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50:
    print("Less than 50")
elif i > 50:
    print("Greater than 50")

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(["orange", "strawberry", "banana"])
print(picked_fruit)

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiply(a: int, b: int) -> int:
    return a * b


# TODO: Now call the function a few times to calculate the following answers

print(multiply(12, 96))
print(multiply(48, 17))
print(multiply(196523, 87323))

print(
    "12 x 96 =",
)

print(
    "48 x 17 =",
)

print(
    "196523 x 87323 =",
)
