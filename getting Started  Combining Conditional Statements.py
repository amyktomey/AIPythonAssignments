#getting started part 5
print("Combining Conditional Statements")

#Please write a program which asks for the user's name. If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.

#In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.

name = input("Please type in your name:")
if name != "Huey" or "Dewey" or "Louie" or "Morty" or "Ferdie":
    print()
elif name == "Huey" or "Dewey" or "Louie":
    print("I think you might be one of Donald Duck's nephews.")
else:
    if name == "Morty" or "Ferdie":
        print("I think you might be one of Mickey Mouse's nephews.")

#The table below outlines the grade boundaries on a certain university course. Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

points = int(input("How many points [0-100]:"))
if points > 100:
    print("Grade: impossible!")
elif points > 90:  # 90-100    5
    print("Grade: 5")
elif points > 80:  # 80-89    4
    print("Grade: 4")
elif points > 70:  # 70-79    3
    print("Grade: 3")
elif points > 60:  # 60-69    2
    print("Grade: 2")
elif points > 50:  # 50-59    1
    print("Grade: 1")
elif points >=0:  # 0-49    fail
    print("fail")
else:
    if points <0:
        print("Grade: impossible! ")

print()
#Please write a program which asks the user for an integer number. If the number is divisible by three, the program should print out Fizz. If the number is divisible by five, the program should print out Buzz. If the number is divisible by both three and five, the program should print out FizzBuzz.

number = int(input("Please input an integer number: "))
if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print()

print()
#Generally, any year that is divisible by four is a leap year. However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

#Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not.

year = int(input("Please type in a year: "))
if year % 4 == 0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

print()        

#Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.
# You may assume the letters will be either all uppercase, or all lowercase.

letter1 = input("PLease enter the first letter:")
letter2 = input("PLease enter the second letter: ")
letter3 = input("PLease enter the third letter: ")
#put letters in alpha order
letters = (letter1, letter2, letter3)
alpha_order=sorted(letters)
print(f"1st letter: {letter1}")
print(f"2nd letter: {letter2}")
print(f"3rd letter: {letter3}")
print(f"The letter in the middle is {alpha_order[1]}")


#Some say paying taxes makes Finns happy, so let's see if the secret of happiness lies in one of the taxes set out in Finnish tax code.
#According to the Finnish Tax Administration, a gift is a transfer of property to another person against no compensation or payment. If the total value of the gifts you receive from the same donor in the course of 3 years is €5,000 or more, you must pay gift tax.
# When the gift is received from a close relative or a family member, the amount of tax to be paid is determined by the following table, which is also available on this website:

""" Value of gift	Tax at the lower limit	Tax rate for the exceeding part (%)
5 000 —  25 000	        100	                     8
25 000 — 55 000	        1 700	                10
55 000 — 200 000	    4 700	                12
200 000 — 1 000 000	    22 100	                15
1 000 000 —	142         100	                    17
So, for a gift of 6 000 euros the recipient pays a tax of 180 euros (100 + (6 000 - 5 000) * 0.08). Similarly, for a gift of 75 000 euros the recipient pays a tax of 7 100 euros (4 700 + (75 000 - 55 000) * 0.12). """

#Please write a program which calculates the correct amount of tax for a gift from a close relative. Have a look at the examples below to see what is expected. Notice the lack of thousands separators in the input values - you may assume there will be no spaces or other thousands separators in the numbers in the input, as we haven't yet covered dealing with these.


gift = int(input("How much is you gift? "))

if gift > 1000000:
    taxes = 142000 + ((gift - 1000000) * .17)
elif gift > 200000:
    taxes = 22100 + ((gift - 200000) * .15)
elif gift > 55000:
    taxes = 4700 + ((gift - 55000) * .12)
elif gift > 25000:
    taxes = 1700 + ((gift - 25000) * .10)
elif gift > 5000:
    taxes = 1700 + ((gift - 25000) * .8)
else:
    if gift < 5000:
        print(f"Value of gift: {gift}")
        print("No tax!")
        print()
        exit

print(f"Value of gift: {gift}")
print(f"Amount of tax: {taxes} euros")
