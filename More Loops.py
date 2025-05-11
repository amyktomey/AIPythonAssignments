""" Please write a program which asks the user for a positive integer number. The program then prints out a list of multiplication operations until both operands reach the number given by the user. See the examples below for details: """

""" Please type in a number: 5
2
1
4
3
5

Sample output

Please type in a number: 6
2
1
4
3
6
5 """

number = int(input("Please type in a number: "))
while number > 0:
    i = 0
    while i < number:
        print(f"{i} ", end="")
        i += 1
    print()
    number -= 1