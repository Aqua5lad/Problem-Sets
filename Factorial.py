# Exercise 6

# Colm Doherty, 2018-03-31
# Purpose: Write a Python script containing a function called factorial()that
# takes a single input/argument which is a positive integer and returns its factorial.
# Test the function by calling it with the values 5, 7, and 10.


def factorial(x):   # Create an input for the calculation that will generate the answer
    answer = 1     #  Assign a starting answer value for the calculation loop

    for i in range(1, x+1):  
        # define a range from the starting value up to the input value for factorial
        # coded in the print statements below.
        answer *= i
        # define the operator for each step (in this case multiplication)
    return answer 

print("Factorial 5 is:", factorial(5))
print("Factorial 7 is:", factorial(7))
print("Factorial 10 is:", factorial(10))
        # print the answers, calling the function for each input value
    
    
