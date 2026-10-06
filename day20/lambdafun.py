

square =lambda x : x**2

print(square(4))

cube = lambda x:x**3
print(cube(5))

sqrt = lambda x:x**0.5

print(sqrt(9))



#definition for finding length 

le=lambda x:len(x)
print(le('sreejith'))


#definition for  getting names from dict
d={
    'name':'sreejith'
}
name=lambda d: d['name']
print(name(d))

#definiton for finding first char of string

f=lambda s:s[0]
print(f('sree'))


#defintion for finding last element of an list
l=[12,3,4]
last=lambda l:l[-1]
print(last(l))

#defintion for finding sum of 2 nums

sum2=lambda x,y:x+y
print(sum2(2,4))

#defintion for finding sum of 3 nums\

sum3=lambda x,y,z:x+y+z

print(sum3(2,4,8))
#definition for fiding prod of nums

prod=lambda a,b,c,d:a*b*c*d
print(prod(2,3,4,7))


#higher order functions



#map

import math
l=[1,2,3,4,5]

print(list(map(lambda x:x**2,l)))
print(set(map(lambda x:x**2,l)))

l1=[1,2,3,4]
#create an new list with cubes
print(list(map(lambda x:x**3,l1)))



#create an new  list with square roots
l2=[25,36,49,64]

print(list(map(lambda x:x**0.5,l2)))

#create new list of length


colors=['red','green','yellow']

print(list(map(lambda x:len(x),colors)))


print(list(map(lambda x:x[0],colors)))

print(list(map(lambda x:x[-1],colors)))


print(list(map(lambda x:x[::-1],colors)))




##given a list of dictionaries
l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]

# # create a new list of emails

print(list(map(lambda x:x['email'],l)))