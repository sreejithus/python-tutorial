# #check an num is 2,3 or 4 digit

# num=int(input('enter an number'))

# num=str(num)

# if (len(num)==2):
#      print('num is 2 digit')
# elif(len(num)==3):
#      print('num is 3 digit')
# elif(len(num)==4):
#      print('num is 4 digit')
# else:
#      print('invalid input')


# #arithematic calculator

# num1=int(input('enter the operand1:'))
# num2=int(input('enter the operand2:'))
# operation=input('opearation:')


# if operation=='+':
#      print(num1+num2)
# elif operation=='-':
#      print(num1-num2)
# elif operation=='*':
#      print(num1-num2)
# elif operation=='/':
#      print(num1-num2)
# else:
#      print('invalid operation')


# #write an prgm to print num of days in month

# month=input('enter the month').lower()

# l1=['january','march','may','july','august','october','decemeber']
# l2=['april','june','september','november']

# if (month in l1):
#      print('31 days')
# elif (month in l2):
#      print('30 days')
# elif month=='february':
#      print('28/29 days')
# else:
#      print('invalid month')



marks=int(input("enter the mark of an student"))

if( marks>=91 and marks<=100 ):
         print('grade A')
elif(marks>=81 and marks<=90):
     print('grade B')
elif(marks>=71 and marks<=80):
     print('grade C')
elif(marks>=61 and marks<=70):
     print('grade D')
elif(marks<61):
     print('grade E')
else:
     print('invalid input')