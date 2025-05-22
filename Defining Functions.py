""" Please write a function named seven_brothers. When the function is called, it should print out the names of the seven brothers in alphabetical order, as in the example below. """

""" Sample output

Aapo
Eero
Juhani
Lauri
Simeoni
Timo
Tuomas """

""" The exercise contains the outline of the function first_character. Please complete it so that it prints out the first character of the string it takes as its argument. """

def first_character(text):
     print(text[0], end=" ")
    

# testing the function:
if __name__ == "__main__":
    first_character('python')
    first_character('yellow')
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')
print()

"""     Please write a function named mean, which takes three integer arguments. The function should print out the arithmetic mean of the three arguments. """

def mean(num1, num2, num3):
     result = ((num1 + num2 + num3)/3)
     print(result)

# testing the function:
mean(5, 3, 1)
mean(10, 1, 1)

""" Please write a function named print_many_times(text, times), which takes a string and an integer as arguments. The integer argument specifies how many times the string argument should be printed out: """

def print_many_times(text, times):
     print((text + "\n")* times)
  
print_many_times("hi", 5)
print()
print_many_times("All Pythons, except one, grow up", 3)


""" Please write a function named hash_square(length), which takes an integer argument. The function prints out a square of hash characters, and the argument specifies the length of the side of the square. """

def line(number, string):
    print(string * number)

def hash_square(length):
     side = length
     while side > 0:
          print(length * "#")
          side -= 1

hash_square(3)
print()
hash_square(5)


""" Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. The function takes an integer argument, which specifies the length of the side of the board. See the examples below for details: """

def chessboard(length):
     lineA = ""
     lineB = ""
     for i in range(length):
          if i%2 == 0:
               lineA += "1"
               lineB += "0"
          else:
               lineA += "0"
               lineB += "1"
     
     for i in range(length):
          if i%2 == 0:
               print(lineA)
          else:
               print(lineB)


chessboard(3)
print()
chessboard(6)

print()

""" Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters as specified by the examples below. """

def squared(string, number):
     size = number
     while size > 0:
          print(number * string)
          size -= 1     

squared("ab", 3)
print()
squared("aybabtu", 5)
