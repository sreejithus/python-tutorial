# for i in range(5):
#      print(i)

# else:
#      print('loop completed')


#write an prgm  to check whether an numbers is prime


# n=int(input('enter the number'))
# if n>1:
#   for i in range(2,n//2):
#      if n%i==0:
#           print('num is not prime')
#           break
#      else:
#          print('prime')

# else:
#     print('num is neither composite or prime')


#perfect number 

n=int(input('enter an number'))
sum=0
for i in range(1,n):
    if n%i==0:
         sum+=i

if n == sum:
    print('num is perfect')
else:
    print('num is not perfect')