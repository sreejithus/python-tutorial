#write a program to find BMI(Body Mass Index)
#
# BMI= weight in (kg)/ height**2 in (m)
#
#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese



Weight=int(input('Enter your weight in kg'))
height=int(input('Enter your height in cm '))
height/=100
BMI=Weight/(height**2)

if (BMI<=18.4):
    print('Underweight')
elif(18.5<=BMI<=24.9):
    print('Normal')
elif(25<=BMI<=39.9):
    print('Overweight')
else:
    print('Obese')

#2.# A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.
code=int(input('Enter the product code'))
price=int(input('Enter the price'))

if (code==1):
    if(price>1000):
        discount=price*(10/100)
        print('your price after discount is',price-discount)
    else:
        print(price)
elif(code==2):
    if(price>100):
           discount=price*(5/100)
           print('your price after discount is',price-discount)
    else:
        print(price)
elif(code==3):
    if(price>500):
           discount=price*(10/100)
           print('your price after discount is',price-discount)
    else:
        print(price)
else:
    print('invalid code')

#3 FIZZBUZZ PRoblem

# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number


num=int(input('enter the number'))

if (num%3==0):
    if(num%5==0):
        print('fizzbuzz')
    else:
        print('fizz')
elif (num%5==0):
       print('buzz')
else:
     print(num)