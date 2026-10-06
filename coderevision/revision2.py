#write an prgm to find maximum number in list 

l=[23,78,45,70,12,56]
max=l[0]

for i in l:
    if max<i:
        max= i


print(max)

min=l[0]

for i in l:
    if min>i:
        min = i


print(min)