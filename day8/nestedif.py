#check whether an number postive odd or even number or negative even/odd


# num=int(input('enter an number'))


# if (num>0):
#      if(num%2==0):
#            print('positive even')
#      else:
#          print('positive odd')
# else:
#       if(num%2==0):
#            print('negative even')
#       else:
#          print('negative odd')



#check whether an num is 
#divisible by 2 and 3
#divisble by 2 and not by 3
#divisible by 3 and not by 2

#not divisible bt 3 and 2


num=int(int('enter an number'))


if (num%2==0):
     if(num%3==0):
          print('num is divisible by 2 and 3')
     else:
          print('num is divible by 2 not by 3')
elif(num%3==0):
       print('num is divisible by 3 not by 2')
else:
     print('not divisible by 2 and 3')