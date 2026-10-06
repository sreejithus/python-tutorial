#given 
l=[1,2,3,4]


new={i:i**2 for i in l}
print(new)



#given an list
l1=[1,2,3,5]

#create an dictionary where keys are index of each number and values are from not list

d={i:l1[i] for i in range(len(l1))}

print(d)

s="python coding  is easy and fun"

d1={i:len(i) for i in s.split() }

print(d1)
