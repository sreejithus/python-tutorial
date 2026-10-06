l1=[1,5,4,3,2]

for i in range(len(l1)):
     for j in range(i+1):
          if l1[i]<l1[j]:
               l1[i],l1[j]=l1[j],l1[i]
print(l1)