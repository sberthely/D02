#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body


def print_horizontal_complete(num_columns):
	for y in range(0,num_columns):
		print('+', end=' ')
		for x in range (0,4):
			print('-', end=' ')
	print('+')

def print_horizontal_incomplete(num_columns):
	for y in range(0,num_columns):
		print('|', end=' ')
		for x in range (0,4):
			print(' ', end=' ')
	print('|')

def print_square(num_columns, num_rows):
	for y in range(0,num_rows):
		print_horizontal_complete(num_columns)
		for x in range (0,4):
			print_horizontal_incomplete(num_columns)
	print_horizontal_complete(num_columns)






# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    print_square(2, 2)
    print_square(4, 4)



if __name__ == "__main__":
    main()