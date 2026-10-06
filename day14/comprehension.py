
l=[1,2,3,4]
 

new=[i**2 for i in l]

print(new)


#given an list 
l1=[12,45,34,67]
#create an new list with even numbers

new1=[i for i in l1 if i%2==0]

print(new1)

#create an a new list values greater than 50

new2=[i for i in l1 if i>50]


print(new2)

#Given  a list 
colors=['red','green','blue','orange']
# create a new list with first letter of each color
new3=[x[0] for x in colors]
# create a new list with length of each color
new4=[len(i) for i in colors]

print(new4,new3)