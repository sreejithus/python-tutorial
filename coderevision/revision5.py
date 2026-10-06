# Define a function that takes a number as an argument and returns True if the number is a Strong Number. Otherwise, return False.
# A number is a Strong Number if the sum of the factorials of its individual digits equals the number.
# Example: 145
# 1! = 1
# 4! = 24
# 5! = 120
# 1 + 24 + 120 = 145
# So, 145 is a Strong Number.


import math
def isstrong(num):

     sum=0
     for i in str(num):
           sum+=math.factorial(int(i))

     if num ==sum:
          print('strong number')
     else:
          print('Not strong number')


isstrong(148)
