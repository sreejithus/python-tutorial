
# Q.Write Python Programs Using map(), filter(), or reduce()
#
# 1.Capitalize all names in a list
names = ['alin', 'arun', 'anu']

n=list(map(lambda x:x.capitalize(),names))
print(n)


# 2.Append "@gmail.com" to a list of usernames
users = ['user1', 'user2']
emails= list(map(lambda x:x+"@gmail.com",users))
print(emails)
# 3.Filter out all empty strings from a list
words = ['hello', ' ', 'world', ' ', 'python']

w=list(filter(lambda x:x!=' ',words))
print(w)
# 4.Filter names that start with the letter 'A'
names = ['Anu', 'Neenu', 'Arun', 'Ravi']

A= list(filter(lambda x:x[0]=='A',names))
print(A)

# 5.Concatenate all strings in a list
words = ['Python', 'is', 'fun']
import functools as ft
sentence=ft.reduce(lambda x,y:x+y,words,'')
print(sentence)


# 6.Multiply all numbers in a list
nums = [2, 3, 4]

prdt=ft.reduce(lambda x,y:x*y,nums,1)

print(prdt)
# 7.Extract First Character of Each Word
words = ["apple", "banana", "cherry"]
ch= list(map(lambda x:x[0],words))
print(ch)

# 8.Add 10 to Each Number
nums = [5, 10, 15]

n1= list(map(lambda x:x+10,nums))
print(n1)
# 9.Given a list
l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
    # #Sum of positive even numbers
pes= ft.reduce(lambda x,y:x+y,filter(lambda x:x>0 and x%2==0,l),0)
print(pes)
    # #Sum of Positive Odd numbers
pos= ft.reduce(lambda x,y:x+y,filter(lambda x:x>0 and x%2!=2,l),0)
print(pos)
    # #Sum of Negative  odd numbers
nos= ft.reduce(lambda x,y:x+y,filter(lambda x:x<0 and x%2!=2,l),0)
print(nos)
    # #Sum of Negatve Even numbers
nes= ft.reduce(lambda x,y:x+y,filter(lambda x:x<0 and x%2==0,l),0)
print(nes)
    # #Count of Positive numbers
pc= list(filter(lambda x:x>0,l))
print(len(pc))

    # #Count of negative numbers
nc= list(filter(lambda x:x<0,l))
print(len(nc))

# 10.Given a list
nums = ["1", "2", "3", "4"]
# Convert all Strings to Integers [1,2,3,4]

inte= list(map(lambda x:int(x),nums))
print(inte)
# 11.
p= [{'name':'laptop','price':50000},
    {'name':'phone','price':20000},
    {'name':'watch','price':3000},
    {'name':'Tablet','price':25000}]

#print list of product names in Uppercase

pnames=list(map(lambda x:x['name'].upper(),p))

print(pnames)


#print products with price greater than 10000

prdts= list(map(lambda x:x['name'],filter(lambda x:x['price']>10000,p)))

print(prdts)

#Find the total price of all products

sum = ft.reduce(lambda x,y:x+y,map(lambda x:x['price'],p),0)

print(sum)


l=[12,-4,78,-34,90,45,16,26,-2,-11,3]

c= ft.reduce(lambda x,y:x+1,filter(lambda x:x>0,l),0)
print(c)


