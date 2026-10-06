#count of all palindrom numbers in range (1,1000)

i=1
count=0
while(i<=1000):
           s=str(i)
         
           if (s==s[::-1]):
                count+=1
           i+=1
print(count)