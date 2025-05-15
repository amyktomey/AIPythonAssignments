""" Please write a function named line, which takes two arguments: an integer and a string. The function prints out a line of text, the length of which is specified by the first argument. The character used to draw the line should be the first character in the second argument. If the second argument is an empty string, the line should consist of stars. """

def line(number, string):
    print(string * number)


#test the code
line(7, "%")
line(10, "LOL")
line(3, "")


""" Please write a function named box_of_hashes, which prints out a rectangle of hash characters. The function takes one argument, which specifies the height of the rectangle. The rectangle should be ten characters wide.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in your line function.
 """
def line(number, string):
    print(string * number)

def box_of_hashes(total):
    while total > 0:
        line(10, "#")
        total -= 1 
    
 
box_of_hashes(5)    
print()
box_of_hashes(2)

print()

""" Please write a function named square_of_hashes, which draws a square of hash characters. The function takes one argument, which determines the length of the side of the square.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function. """

def line(number, string):
    print(string * number)

def square_of_hashes(total):
    number = total
    while total > 0:
        line(number, "#")
        total -= 1

square_of_hashes(5)
print()
square_of_hashes(3)

""" Please write a function named square, which prints out a square of characters, and takes two arguments. The first parameter specifies the length of the side of the square. The second parameter specifies the character used to draw the square.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function. """

def line(number, string):
    print(string * number)

def square(length, string):
    number = length
    while length > 0:
        line(number, string)
        length -= 1

square(5, "*")
print()
square(3, "o")

""" Please write a function named triangle, which draws a triangle of hashes, and takes one argument. The triangle should be as tall and as wide as the value of the argument.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function. """

def line(number, string):
    print(string * number)

def triangle(height):
    for number in range(height):
        line(number, "#")

triangle(6)
print()
triangle(3)

""" Please write a function named shape, which takes four arguments. The first two parameters specify a triangle, as above, and the character used to draw it. The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. The fourth parameter specifies the filler character of the rectangle. The function prints first the triangle, and then the rectangle below it.
 """

def line(number, string):
    print(string * number)

def shape(width, char, height, filler ):
    for number in range(width):
        line(number, char)
    
    number = height
    while height != 0:
        line(number, filler)
        height -= 1
    
shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")

""" A spruce
Please write a function named spruce, which takes one argument. The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument."""

def spruce(height):
    print("a spruce")
    for number in range(height):
       print (" " *(height-number) + "*"*(2*number-1))
    print (" " * (height-1) + "*")

spruce(3)
spruce(5)


# Calling spruce(3) should print out:

# Sample output
# a spruce!
#   *
#  ***
# *****
#   *
# Calling spruce(5) should print out:

# Sample output
# a spruce!
#     *
#    ***
#   *****
#  *******
# *********
#     *
""" NB: To the left of the spruce there should be exactly the right amount of whitespace. If the shape of the spruce looks correct, but the left edge of the tree is not touching the left edge of the text area in the terminal, the tests will not accept the solution. " """""

""" Please write a function named greatest_number, which takes three arguments. The function returns the greatest in value of the three. """

# def greatest_number(num1, num2, num3):

#test the code
# (greatest_number(3, 4, 1)) # 4
# (greatest_number(99, -4, 7)) # 99
# (greatest_number(0, 0, 0)) # 0