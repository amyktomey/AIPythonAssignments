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

