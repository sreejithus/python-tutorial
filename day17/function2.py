#define an function that takes a list of argument

#return new list containing unique element fromn the list

def unique(l):
    new=[]
    for i in l:
        if  i not in new:
            new.append(i)
    return new

l=[12,34,67,12,34,19,23]

l1=unique(l)
print(l1)

def common(l1,l2):
    for i in l1:
        if i in l2:
            print(i)

l1=[12,34,56,78,90]

l2=[90,34,11,57,45]

common(l1,l2)

#
def fun(n,a):
    print('name',n)
    print('age',a)

fun(n='sreejith',a=21)

def fun(*args):
    print(args)


fun(1,2,3,4,5)

def fun(**args):
    print(args)

fun(name='sreejith',age=23)

#define an function that accepts any number of numbers and returns their sum

def sums(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(sums(1,2,3,4,5))


import math




print(abs(-34))

print(max((1,3,4,5,6,7,7)))

print(min((1,2,3,4,)))

print(round(2.455,2))

print(divmod(8,2))

print(sum((1,23,4,5,5)))

print(pow(2,3))


print(math.sqrt(36))

print(math.isqrt(36))
print(math.factorial(5))

print(math.floor(3.6))

print(math.gcd(55,45))

print(math.lcm(34,89))

import random

print(random.random())#generate floating point nums 0 to 1

print(random.randint(1,100))


print(random.randrange(100,999,2))

print(random.randint(10000,9999))


print(random.choice((1,2,4,5)))