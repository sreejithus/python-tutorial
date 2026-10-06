# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input



import math

try:
    n = int(input('enter an number'))
    print(math.factorial(n))


except ValueError:
    print('invalid input')
    










# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.


try:

 while True:

     print('choose an option ')
     print('1.Add 2.Difference 3.Division 4.Multiplication')
     n = int(input('enter your choice'))

     if n == 1:
        a= int(input('enter the num1 : '))
        b =int(input('enter the num2: '))
        print(a+b)
     elif n ==2:
          a= int(input('enter the num1 : '))
          b =int(input('enter the num2: '))
          print(a-b)
     elif n == 3:
         a= int(input('enter the num1 : '))
         b =int(input('enter the num2: '))
         print(a/b)
     elif n == 4:
             a= int(input('enter the num1 : '))
             b =int(input('enter the num2: '))
             print(a*b)
     else:
         print('invalid choice')
        
    

except ZeroDivisionError:
    print("you can't divide using zero")
except ValueError:
    print('invalid value ')

except Exception:
    print(Exception)








# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist


try:

    f = open('hi.txt','r')
    f.read()

except FileNotFoundError:
     print('file not exist')