from collections import Counter

num=[2,1,6,4,3]
target=5

seen = {}
for i in range(len(num)):
         num1=num[i]
         need = target-num1
         if need in seen:
             print(seen[need],i)
             break
         seen[num1]=i
       
    

     