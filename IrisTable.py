# Exercise 5

# Colm Doherty on 2018-03-05
# Exercise 5 - a python script that reads the Iris dataset and prints 
# the four numerical values on each row in an nice format, so, petal length,
# petal width, sepal length, sepa width, with decimal places aligned and 
# a space between the columns. 

with open("data/iris.csv") as f:
            # open(filename) returns the file to be used, in this case the Iris dataset.
            # For best practice, its prefaced by 'with' to ensure the file is closed afterwards

    for line in f:        
            # for each line in the dataset:

        print('{:4} {:4} {:4} {:4}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
        
            # split it into its four constituent elements (petal length, petal width, sepal length, sepa width) and
            # add the data for each, using the {:n} syntax to give each printed element a width of n, where n is {:n}
                

                
# When you're chewing on life's gristle, Don't grumble, give a whistle   
