# Exercise 6

# Colm Doherty, 2018-03-31
# Purpose: Write a Python script containing a function called factorial()that
# takes a single input/argument which is a positive integer and returns its factorial.
# Test the function by calling it with the values 5, 7, and 10.


def factorial(x):
    answer = 1
    for i in range(1, x + 1):
        answer *= i
    return answer 

print("Factorial 5 is:", factorial(5))
print("Factorial 7 is:", factorial(7))
print("Factorial 10 is:", factorial(10))
