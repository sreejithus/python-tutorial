# #Write a program to check whether two entered numbers are equal or not
num1=int(input('enter the num1'))
num2=int(input('enter the num2'))

if(num1==num2):
    print('numbers are equal')
else:
     print('numbers are not equal')


# #Write a program to check whether two entered words are equal or not
word1=input('enter the word1')
word2=input('enter the word2')

if(word1==word2):
    print('words are equal')
else:
     print('words are not equal')


# #Write a program to find the maximum of two numbers
num1=int(input('enter the num1'))
num2=int(input('enter the num2'))

if (num1>num2):
     print('num1 is greater')
else:
        print('num2 is greater')


# #write a program to check whether the entered character is vowel or not

ch=input('enter the character')
vowels='aeiouAEIOU'

if (ch in vowels):
     print('vowel')
else:
     print('not an vowel')
# #Write a program to check whether the entered country name contains word 'land'
loc=input('enter the country name')

if('land' in loc):
     print('contains land')
else:
     print('not contains land')
# #write a program to check whether the entered number is 3 digit or not
num=int(input('enter an num '))
num= str(num)

if(len(num)==3 ):
     print(num,'is an 3digit number')
else:
      print(num,'is  not an 3digit number')
#write a program to check whether the entered string is  palindromde or not

s=input('enter the string')
if (s[::-1]==s):
     print('palindrome')
else:
     print('not palindrome')
#Write a program to check whether a number is present in given list
l=[23,67,12,90]

num=int(input('enter the num'))

if (num in l):
     print('num is present')
else:
     print('num is not present')
#Write a program to check whether a key is prsent in a dictionary or not
d={101:'Arun',102:'Amal',103:'Anu'}
key=int(input('enter the key'))

if(key in d):
     print('key is present')
else:
     print('key is not present')
#Write a program to check whether the given pasword is strong/weak(if length lessthan 8 weak)

password=input('enter the password')

if (len(password)<8):
     print('weak password')
else:
     print('strong password')