# for i in range(5):
#      print(i)

# else:
#      print('loop completed')


#write an prgm  to check whether an numbers is prime


n=int(input('enter the number'))

for i in range(2,n-1):
     if n%i==0:
          print('num is not prime')
          break
else: