# Exercise 5

# Colm Doherty on 2018-03-05
# Exercise 5 - a python script that reads the Iris dataset and prints 
# the four numerical values on each row in an nice format, so, petal length,
# petal width, sepal length, sepa width, with decimal places aligned and 
# a space between the columns. 

with open("data/iris.csv") as f:
    for line in f:        
        print('{:4} {:4} {:4} {:4}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
