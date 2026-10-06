#find the first character that appears only once 
from collections import Counter

s=input("enter the word").lower()

d1=Counter(s)

for i in s:
    if d1[i]==1:
        print(i)
        break
  

