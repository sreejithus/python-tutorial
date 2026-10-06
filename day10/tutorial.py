#count of those numbers that are divisible by 3 in the range of 1,50


# i=1
# count=0
# while(i<=50):
#      if(i%3==0):
#              count+=1
#      i+=1
# print(count)


#sum of series 1,2,3,4,5

i=1
sum=0

while(i<=5):
         sum+=i
         i+=1

print(sum)


##sum of all nums that are 3 digit
i=100

sum=0
while(i<=999):
         sum+=i
         i+=1

print(sum)

#sum of nums that are even range of 1,20
i=2

sum1=0
while(i<=20):
         sum1+=i
         i+=2

print(sum1)


#sum of nums that are divisible by 3 in range of 1,50
i=1
sum=0
while(i<=50):
     if(i%3==0):
             sum+=i
     i+=1
print(sum)

#product of 1,2,3,4,5


i=1
prdt=1

while(i<=5):
     
     prdt*=i
     i+=1
print(prdt)

#prdt of nums that contains digit '3' in range of 1,50

i=1
prdt=1

while(i<=50):
        if ('3' in str(i)):
                     prdt*=i
        
        i+=1

print(prdt)
#prdt of first 10 odd nums 
# 
i=1

sum1=1
while(i<=20):
         sum1*=i
    
         i+=2

print(sum1)


#factorial of num

num=int(input('enter the number'))
fact=1
i=1

while(i<=num):
        fact*=i
        i+=1
print(fact)


#multiplication table of an number 


num=int(input('enter an number'))


i=1
while (i<=10):
         
         print(num,"*",i,"=",num*i)
         i+=1