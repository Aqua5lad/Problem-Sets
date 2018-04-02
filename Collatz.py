# Exercise 3

# the Collatz conjecture, or n = 3n+1
# written by Colm Doherty on 2018-02-08

# This function returns the Collatz sequence for 'n' until it falls to 1
# The Collatz Conjecture states that, starting with a positive Integer,
# if the previous term is even, and you divide it by 2, or if it is
# odd, and you multiply it by 3 and add 1, then no matter what term 
# you start with, the sequence will always reach 1. 

n = 27
print (n)

while n <=10000 and (n != 1) :
    if (n % 2 == 0): 
        n = n//2
        print (n)
    else:
        n = (n*3)+1
        print (n)
