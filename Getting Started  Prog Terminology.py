print("From Programming Terminology")

print()
#The following program contains several syntactic errors. Please fix the program so that the syntax is in order and the program works as specified by the examples below.
number = int(input("Please type in a number: "))
if number > 199:
  print("The number was greater than one hundred")
  print("Have a nice day!")
elif number > 100:
  number - 100
  print("Now its value has decreased by one hundred")
  print(F"Its value is now {number}")
  print(F"{number} must be my lucky number!")
  print("Have a nice day!")
else:
  print(F"{number} must be my lucky number!")
  print("Have a nice day!")


#Please write a program which asks the user for a word and then prints out the number of characters, if there was more than one typed in.

word = input('Please type in a word: ')
count = len(word)
while count > 1:
  print(f'There are {count} letters in the word {word}')
  break
print('Thank you!')


#When programming in Python, often we need to change the data type of a value. For example, a floating point number can be converted into an integer with the function int:

""" print("The temperature is", temperature)

print("...and rounded down it is", int(temperature))
Sample output

Please type in a temperature: 5.15
The temperature is 5.15
...and rounded down it is 5

Sample output

Please type in a temperature: 8.99
The temperature is 8.99
...and rounded down it is 8 """

#Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. Use the Python int function. You can assume the number given by the user is always greater than zero.

""" An example of expected behaviour:

Sample output
Please type in a number: 1.34
Integer part: 1
Decimal part: 0.34 """

