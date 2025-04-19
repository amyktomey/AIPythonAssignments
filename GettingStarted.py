print()
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print("my name is", name, " , I am ", age, "years old")
print("my skills are")
print(f"- skill1 ({level1})")
print(f"- skill2 ({level2})")
print(f"- skill3 ({level3})")
print()
print("I am looking for a job with a salary of", lower, "-", upper, "euros per month")

print()

print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4, end="")

print()
print()
days = int(input("How many days? "))
seconds = days * 86400
minutes = int(seconds/60)  #adeded minutes to the calculation
print(f"Seconds in that many days: {seconds}")
print(f"Minutes in that many days: {minutes}")

print()

#Please write a program which asks the user for an integer number. The program should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.

number = int(input("Please type in a 4 digit number: "))
if number == 1984:
    print("Orwell")
else:
    print()

print()
#Please write a program which asks the user for an integer number. If the number is less than zero, the program should print out the number multiplied by -1. Otherwise the program prints out the number as is.

number = int(input("Please type in a number: "))
if number < 0:         
    print(number * -1)      
else:
    print(number)

print()
#Please write a program which asks for the user's name. If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. The price of a single portion is 5.90.

name = input("What is your name? ")
if name == "Jerry":
    print("Next please?")
else:
    count=int(input("How many portions wuold you like? "))
    total = count * 5.90
    print(f"Total cost for {count} portions: ${total}")
    print("Next please?")

print()
#Please write a program which asks the user for an integer number. The program should then print out the magnitude of the number according to the following examples.

number = int(input("Please type in a number: "))

if number < 1000 and 100 and 10:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")
    print("Thank You!")
elif number < 1000 and 100:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("Thank You!") 
elif number < 1000:
    print("This number is smaller than 1000")
    print("Thank You!")   
else:
    print("Thank You!") 

print()
