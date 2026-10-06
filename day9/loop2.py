# #print the  3 digit nums that are divisible by 3

# i=100

# while(i<=999):
#     if(i%3==0):
#         print(i)
#     i+=1


# #print those  4 digit nums that contains digit '3' 

# i=1000

# while(i<=9999):
#     i=str(i)
#     if '3' in i:
#         print(int(i))
#     i=int(i)+1

# #print those numbers that are divisible by 3 and 5 in range 1,100
# i=1

# while(i<=100):
#     if(i%3==0 and i%5==0):
#         print(i)
#     i+=1

# #1,4,9,16,25


# i=1

# while(i<=10):
#     print(i**2)
#     i+=1


#print count of  3 digit nums that contains digit '3'  

i=100
count=0
while(i<=999):

    if '3' in str(i):
        
        count+=1
    i=i+1
print(count)


i=1
count=0
while(i<=100):
     if(i%3==0 or i%7==0):
         count+=1
     i+=1

print(count)


i=1
count=0
while(i<=100):
     if(i%2!=0 and i%5==0):
         count+=1
     i+=1

print(count)


