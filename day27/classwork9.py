 #1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
#
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
#
# Create an object of the Circle class and call both methods to display the results.
#
# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.

import math

class circle:
    def __init__(self):
        self.radius=int(input('enter the radius'))

    def getarea(self):
        return (self.radius**2)*(math.pi)

    def getperimeter(self):
        return (self.radius*2)*(math.pi)


Circle = circle()

print(Circle.getarea())
print(Circle.getperimeter())




class Account:
    def __init__(self):
         self.accountnumber=input('enter the accountnumber')
         self.acctname=input('enter the accountname')
         self.balence=int(input('enter the balence'))

    def withdraw(self):
        amount=int(input('enter the amount to withdraw'))
        self.balence = self.balence-amount
        print("your current balence is ",self.balence)
    def deposite(self):
        amount=int(input('enter the amount to deposite'))
        self.balence = self.balence+amount
        print("your current balence is ",self.balence)
    def showbalence(self):
          print("your current balence is ",self.balence)



a=Account()
b=Account()
l=[a,b]



for i in l:
      print(f"account number :{i.accountnumber} Name:{i.acctname} balence: {i.balence}  ")


#print the balence of the person whose number matches with the accountnumber
number=input('enter the accout number')
for i in l:
     if i.accountnumber == number:
          print("Balence is",i.balence)