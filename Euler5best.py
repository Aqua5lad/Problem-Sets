# Exercise 4

# Colm Doherty on 2018-02-22, based on an approach suggested by Chris Johnson at
# https://stackoverflow.com/questions/31840761/project-euler-5-using-python
# it works, but it takes 3 mins to print a result. I think it could be optimised, 
# but I have not yet found the time to experiment with it!
# It returns the result as 232792560

# Euler Problem 5 : using for and range to calculate the smallest positive number 
# evenly divisible by all of the numbers from 1 to 20

result = None
n = 2520
# n = smallest value evenly divisible by i. we are told that 2520 is the 
# smallest value evenly disable by range (1,10), so n must be > 2520

while not result:
    n = n + 1
    for i in range(2,21):
        if n % i:
            break

# for as long as no even number results from n / i, keep adding 1 until it does   
    else:
        result = n
# as this is the first even number found, while adding 1 each time, its the lowest one

print("the result is:",result)


# And now for something completely different
