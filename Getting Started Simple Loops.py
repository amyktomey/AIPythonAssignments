#getting started part 6
print("Simple Loops")

#Let's create a program that will print out the message "hi" and then ask "Shall we continue?" until the user inputs "no". Then the program should print out "okay then" and finish. Please have a look at the example below.

print('hi')
answer = input('Shall we continue? ')
while answer != "no":
  print('hi')
  input('Shall we continue? ')
  if answer == 'no':
    break
print("okay then") 


#Please write a program which asks the user for integer numbers.
# If the number is below zero, the program should print out the message "Invalid number".
# If the number is above zero, the program should print out the square root of the number using the Python sqrt function.
# In either case, the program should then ask for another number.
# If the user inputs the number zero, the program should stop asking for numbers and exit the loop.
# Below you'll find a reminder of how the sqrt function is used. Remember to import it in the beginning of the program.

# sqrt function will not work without this line in the beginning of the program

from math import sqrt

integer = int(input('Please type in a number: '))
if integer < 0:
  print('Invalid number')
  print(input('Please type in a number: ')) 
elif integer == 0:
  print("Exiting...")
else: 
  print(sqrt(integer))
 

#This program should print out a countdown. The code is as follows:
# However, the program doesn't quite work. Please fix it.
number = 5
print("Countdown!")
while True:
  print(number)
  number -= 1
  if number == 0:
    break
print("Now!")


#Please write a program which
# Asks for the password.
# Asks for the password again.
# If the two passwords match, prints "Correct!".
# Otherwise prints "They do not match!".

while True:
    password = input("Please type in the password: ")
    password2 = input("Repeat the password: ")
    if password == password2:
        break
    print("They do not match!")

print("Correct!")


#Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. The program should then print out the number of times the user tried different codes.
count = 0
while True:
  code = 4321
  code2 = int(input("Please type in your PIN: "))
  if code == code2:
    break
  count += 1
  print("Incorrect...try again")

if count == 0:
  print("Correct! It only took you one single attempt!")
else:
  print(f"Correct! It took you {count} attempts")



#Please write a program which asks the user for a year, and prints out the next leap year.

inputyear = int(input("please type in a year: "))
year = inputyear
while True:
  year+=1
  if year % 100 == 0:
    if year % 400 == 0:
      break
  elif year % 4 == 0:
    break

print(f"Year: {inputyear}")
print(f"The next leap year after {inputyear} is {year}")

#---------------------------------------------------------------------------------
#Part 1
#Please write a program which keeps asking the user for words. If the user types in end, the program should print out the story the words formed, and finish.

story = ""
while True:
    word = input("Please type in a word: ")
    if(word == 'end'):
        break
    else:
        story += word + " "
if story:
  print(story)
   
#Part 2

#Change the program so that the loop ends also if the user types in the same word twice in a row.

story = ""
prev_word = ""
while True:
    word = input("Please type in a word: ")
    if(word == 'end'):
        break
    elif prev_word.lower() == word.lower():
        break
    else:
        story += word + " "
        prev_word = word
if story:
  print(story)
   

#-----------------------------------------------------------------------------------
#Pre-task
# Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero.

number = int(input("Please type in integer numbers. Type in 0 to finish."))
while number != 0:
  if number != 0:
    print(f"Number: {number}")
  else:
    break
print("Number: 0")

""" Sample output

Please type in integer numbers. Type in 0 to finish.
Number: 5
Number: 22
Number: 9
Number: -2
Number: 0 """

#Part 1: Count

# After reading in the numbers the program should print out how many numbers were typed in. The zero at the end should not be included in the count. You will need a new variable here to keep track of the numbers typed in.

number = int(input("Please type in integer numbers. Type in 0 to finish. "))
count = 0
while True:
  if number != 0:
    print(f"Number: {number}")
    count+=1
  else:
     break
print("Number: 0")
print(f"Numbers typed in {count} ")

""" Sample output

... the program asks for numbers
Numbers typed in 4 """

#Part 2: Sum
# The program should also print out the sum of all the numbers typed in. The zero at the end should not be included in the calculation. 

number = int(input("Please type in integer numbers. Type in 0 to finish. "))
count = 0
numbers = " "
while number != 0:
  print(f"Number: {number}")
  count+=1
  break
total = sum(numbers)
print("Number: 0")
print(f"Numbers typed in {count} ")
print(f"The sum of the numbers is {total} ")


# The program should now print out the following:

""" Sample output

... the program asks for numbers
Numbers typed in 4
The sum of the numbers is 34 """

#Part 3: Mean
# The program should also print out the mean of the numbers. The zero at the end should not be included in the calculation. You may assume the user will always type in at least one valid non-zero number.
number = int(input("Please type in integer numbers. Type in 0 to finish. "))
count = 0
numbers = " "
while number != 0:
  print(f"Number: {number}")
  count+=1
  break
total = sum(numbers)
average = total/len(numbers)
print("Number: 0")
print(f"Numbers typed in {count} ")
print(f"The sum of the numbers is {total} ")
print(f"The mean of the numbers is({average})")

""" Sample output

... the program asks for numbers
Numbers typed in 4
The sum of the numbers is 34
The mean of the numbers is 8.5 """

#Part 4: Positives and negatives
# The program should also print out statistics on how many of the numbers were positive and how many were negative. The zero at the end should not be included in the calculation.

number = int(input("Please type in integer numbers. Type in 0 to finish. "))
count = 0
numbers = " "
while number != 0:
  print(f"Number: {number}")
  count+=1
  break
total = sum(numbers)
average = total/len(numbers)
posnum = 0
for int in numbers:
   if int > 0:
    posnum += 1

print("Number: 0")
print(f"Numbers typed in {count} ")
print(f"The sum of the numbers is {total} ")
print(f"The mean of the numbers is({average})")
print(f"Positive numbers {posnum}")

""" Sample output

... the program asks for numbers
Numbers typed in 4
The sum of the numbers is 34
The mean of the numbers is 8.5
Positive numbers 3 """
