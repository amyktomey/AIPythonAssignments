""" Please write a program which asks the user for a string and an amount. The program then prints out the string as many times as specified by the amount. The printout should all be on one line, with no extra spaces or symbols added. """

string = input("Please type in a string: ")
number = int(input("Please type in an amount: "))
print(string * number)

""" Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long". """

string1 = input("Please type in string 1: ")
string2 = input("Please type in string 2: ")

if len(string1) == len(string2):
    print("The strings are equally long")
elif len(string1) > len(string2):
    print(f"{string1} is longer")
else:
    print(f"{string2} is longer")

""" Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line. """


string = input("Please type in a string: ")
place = 0
index = len(string)
while place < index:
    print(string[index-1])
    index -= 1
print()

""" Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not. """

string = input("Please type in a string: ")

if string[-2] == string[1]:
    print(f"The second and the second to last characters are {string[1]}")
else:
    print("The second and the second to last characters are different")

""" Please write a program which prints out a line of hash characters, the width of which is chosen by the user. """

count = int(input("Enter a number: "))
print(f"Width: {count}")
print(count * "#")
            
""" Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly. """

width = int(input("Enter a number: "))
height = int(input("Enter a number: "))
print(f"Width: {width}")
print(f"Height: {height}")
while height != 0:
    print(width * "#")
    height -= 1
else:
    print()

"""    Please write a program which asks the user for strings using a loop. The program prints out each string underlined as shown in the examples below. The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.  """

newstring = input("Please type in a string:")
length = len(newstring)
while newstring != (""):
    print(newstring)
    print(length*"-")
    newstring = input("Please type in a string:")
else:
    print()

""" Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

You may assume the input string is at most 20 characters long. """

string = input("Please type in a string:")
endstring=len(string)
while endstring > 20:
    firsttwenty = string[:19]
    print(firsttwenty)
    break
else:
    startstring = 19-endstring
    print((startstring*"*" + string))

"""Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations. """

""" Sample output

Word: testing

******************************
*          testing           *
******************************

Sample output """




"""
substring part 1
 Please write a program which asks the user to type in a string. The program then prints out all the substrings which begin with the first character, from the shortest to the longest. Have a look at the example below. """

""" Sample output

Please type in a string: test
t
te
tes
test """

""" substring part 2
Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character, from the shortest to the longest. Have a look at the example below. """


""" Please type in a string: test
t
st
est
test """


""" Please write a program which asks the user to input a string. The program then prints out different messages if the string contains any of the vowels a, e, or o.

You may assume the input will be in lowercase entirely. Have a look at the examples below. """



""" Sample output

Please type in a string: hello there
a not found
e found
o found

Sample output

Please type in a string: hiya
a found
e not found
o not found """