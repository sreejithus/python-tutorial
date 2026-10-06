# # # #Write a program to find the position of a character in a string
s='sreejith'

print(s.index('s'))


# # # #write a program to find the count of character in  a string
c=input('enter the ch')
print(s.count(c))

# # #create a random 5 digit otp number and print otp number
import random

otp =  random.randint(10000,99999)
print(otp)
# #create a list of  5 random 3 digit numbers
new=[]
for i in range(5):
         new.append(random.randint(100,999))

print(new)

# #create a dictionary where keys are words and values are length of each word from the string
#
s="python coding is easy and fun"
d={}
for i in s.split():
        d[i]=len(i)
print(d)
# #new={'python':6,'coding':6,'is':2,'easy':4,'and':3,'fun':3}

# #create a dictionary where keys are each character and values are number of occurence of each character
s="hello world"
d1={}
for i in s:
        if i!=' ':
           d1[i]=s.count(i)

print(d1)

# #write a program to find the number of digits,letters,and spaces in a string

s="sdfghjk3456789  dffghjkl345678"
sp=0
a=0
n=0
for i in s:
        if i.isalpha():
                a+=1
        elif i.isdigit():
                n+=1
        elif i.isspace():
                sp+=1


print('num of alpha',a)
print('num of numbers',n)
print('num of space',sp)

# # Given a list 
l=[['amal',23,30000],['arun',25,50000],['anu',24,40000]]

# # # create a list of salaries
salaries=[]
for i in l:
        salaries.append(i[2])

print(salaries)
        

# # # find the maximum salary

print(max(salaries))

# # # find minimum salary

print(min(salaries))


#Given a dictionary
d={'arun':34,'amal':45,'anu':40,'kiran':25,'manu':30}

# create a new list of students whose mark>=40
new=[]
for i in d:
        if d[i]>=40:
                new.append(i)
print(new)
#Given two lists
l1=[11,27,34,45,56]
l2=[27,34,86,91]
# Find Common elements 

for i in l1:
        if i in l2:
                print(i)
#Given
l=[23,45,67,12,90,56]
#find second largest number 

l.sort(reverse=True)

for i in l:
        if i == max(l):
                continue
        else:
                print(i)
                break


#find second smallest number

l.sort()

for i in l:
        if i == min(l):
                continue
        else:
                print(i)
                break
