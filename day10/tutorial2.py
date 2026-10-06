l1=[12,34,56,45,89,16,69,33]

#print each number in list which is even

for i in l1:
    if(i%2==0):
        print(i)

#print each number in list which is divisible by 5

for i in l1:
    if(i%5==0):
        print(i)

#print each number in list which contains 3

for i in l1:
    if('3'in str(i)):
        print(i)
        
sum=0
for i in l1:
    sum+=i

print(sum)

count=0
for i in l1:
    count+=1

print(count)



count=0
for i in l1:
    if(i%2==0):
         count+=1

print(count)



p=1
for i in l1:
    p*=i

print(p)



for i in l1:
     print(i**2)