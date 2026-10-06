
l1=[1,24,5,6,7]
l2=[1,24,8,7]

s=set(l1).intersection(set(l2))

print(s)

s.update({4,4,5})
print(s)



d={
    'a':20,
    'b':30,
    'c':40
}


print(d.get('a'))

print(d.popitem())


print(d.pop('b'))

d.update({'g':56,'h':78})

print(d)


for i,j in d.items():
    print(i,j)

l=[[1,2],[4,8]]

for i,j in l:
    print(i,j)



def lengthOfLongestSubstring(self, s):
         new=[]
         temp=[]
         for i in s:
             if i in temp:
                 new.append(len(temp))
                 temp=[]
             else:
                 temp.append(i)
         return max(new)