#getting started part 5
print("Combining Conditional Statements")

#Please write a program which asks for the user's name. If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.

#In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.

""" Sample output

Please type in your name: Morty
I think you might be one of Mickey Mouse's nephews.

Sample output

Please type in your name: Huey
I think you might be one of Donald Duck's nephews.

Sample output

Please type in your name: Ken """

#The table below outlines the grade boundaries on a certain university course. Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

""" points    grade
< 0    impossible!
0-49    fail
50-59    1
60-69    2
70-79    3
80-89    4
90-100    5
> 100    impossible!
Sample output

How many points [0-100]: 37
Grade: fail

Sample output

How many points [0-100]: 76
Grade: 3

Sample output

How many points [0-100]: -3
Grade: impossible! """

#Please write a program which asks the user for an integer number. If the number is divisible by three, the program should print out Fizz. If the number is divisible by five, the program should print out Buzz. If the number is divisible by both three and five, the program should print out FizzBuzz.

""" Number: 9
Fizz

Sample output

Number: 7

Sample output

Number: 20
Buzz

Sample output

Number: 45
FizzBuzz
 """

#Generally, any year that is divisible by four is a leap year. However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

#Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not.

""" Please type in a year: 2011
That year is not a leap year.

Sample output

Please type in a year: 2020
That year is a leap year.

Sample output

Please type in a year: 1800
That year is not a leap year. """

#Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.
# You may assume the letters will be either all uppercase, or all lowercase.

""" Sample output

1st letter: x
2nd letter: c
3rd letter: p
The letter in the middle is p

Sample output

1st letter: C
2nd letter: B
3rd letter: A
The letter in the middle is B """

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

""" Sample output

Value of gift: 3500
No tax!

Sample output

Value of gift: 5000
Amount of tax: 100.0 euros

Sample output

Value of gift: 27500 """
