 # #create a new list with square root of each element
from numbers import Number


l=[25,16,9,36]

sqrts=[i**0.5 for i in l]
print(sqrts)


# #Given a dictionary
d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # create a list of names
new=[i for i in d ]
print(new)
# # create a list of marks
new1=[i for i in d.values()]
print(new1)
# #Given a list
l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']

# #create a list of string values
strings=[i for i in l if type(i)==str]
# #create a list of floats
print(strings)
floats=[i for i in l if type(i)==float]
print(floats)
# #create a list of positive numbers
positivenumbers=[i for i in l if (type(i)==int or type(i)==float) and i>0]
print(positivenumbers)
#

# #Given a list
fruits=['apple','orange','pineapple','avocado','grapes']
##create a new list with elements whose length is greater than 6

fruit=[i for i in fruits if len(i)>6]
print(fruit)
# #create a new list with elements whose value is divisible by 3 in range(1,101)

l2=[i for i in range(1,101) if i%3==0]
print(l2)
# Given 
s="python coding  is easy and fun"
# # create a new list with only vowels
 
vowels=[i for i in s if i in 'aeiouAEIOU' ]


print(vowels)


