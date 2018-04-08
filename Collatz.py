# Exercise 3

# the Collatz conjecture, or n = 3n+1
# written by Colm Doherty on 2018-02-08

# This function returns the Collatz sequence for 'n' until it falls to 1.
# The Collatz Conjecture states that, starting with a positive Integer,
# if the previous term is even, and you divide it by 2, or if it is
# odd, and you multiply it by 3 and add 1, then no matter what term 
# you start with, the sequence will always reach 1. We are given a 
# start value for 'n' of 17.

n = 17      #state the given start value
print (n)   #display the chosen start value

while n <=10000 and (n != 1) :
            # while the value is not 1, and less than 10,000 
    if (n % 2 == 0):
            # if its an even number 
        n = n//2
            # divide it by 2
        print (n)
            # and display the result
    else:
            # otherwise it's odd, so
        n = (n*3)+1
            # multiply it by 3 and add 1
            # this loops continually until the value falls to 1
        print (n)
            # display the sequence

# what have the romans ever done for us?
