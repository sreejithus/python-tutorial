# # # Q1.Define a function that takes 2 numbers and returns their product


def product(a,b):
    return a*b

n1=int(input('enter the num1'))
n2=int(input('enter the num2'))
result=product(n1,n2)
print(result)

# # Q2.Define a function that takes a string and returns number of vowels

def vowelcount(s):
    count=0
    for i in s:
        if i in 'aeiouAEIOU':
            count+=1
    return count

print(vowelcount('sreejith'))


# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle

def area(b,l):
    return b*l


length=int(input('enter the length'))
breadth=int(input('enter the breadth'))

print(area(length,breadth))
#
# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]
#


def even(l):
    new=[i for i in l if i%2==0]
    return new

l=[1,2,3,4,6,5]
print(even(l))

# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]


def sumofdigits(l):
    new=[]
    for i in l:
        sum=0
        for j in str(i):
            sum+=int(j)
        new.append(sum)
    return new
l=[123, 345, 111, 678, 134, 809]
print(sumofdigits(l))



