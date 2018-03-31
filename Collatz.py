# Exercise 3

# the Collatz conjecture, or n = 3n+1
# written by Colm Doherty on 2018-02-08

# This function returns the Collatz sequence for 'n' until it falls to 1

n = 27
print (n)

while n <=10000 and (n != 1) :
    if (n % 2 == 0): 
        n = n//2
        print (n)
    else:
        n = (n*3)+1
        print (n)
