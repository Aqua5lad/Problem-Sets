# Exercises 2 and 1

# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.
# Edited by Colm Doherty to return the nth Fibonacci number where n is the sum 
# of the first and last letters of my Surname as numbers.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Doherty"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

# Here is the text I pasted into the discussion forums for weeks 1 and 2 :

# Week 2 Task.
# My surname is Doherty
# The first letter D is number 68
# The last letter y is number 121

# Fibonacci number 189 is 1409869790947669143312035591975596518914

# What ‘Ord()’ does is to return an integer, equivalent to the position of the value in brackets, at its place in the order of ASCII decimals.

# So, in text, D is 68th in the order of ASCII characters and is represented in binary code as 01000100.

# “firstno = ord(first)” means: return, as an integer, the ASCII order value of ‘first’ where ‘first’ has already been defined as name[0] - i.e. the first letter of the value ‘name’

# Week 1 Task.
# My name is Colm, so the first and last letter of my name (C + M = 3 + 13) give the number 16. The 16th Fibonacci number is 987
