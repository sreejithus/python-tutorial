
# def addition():
#      num1=int(input('enter the num1'))
#      num2= int(input('enter the num2'))
#      sum = num1+num2
#      print('sum',sum)


# addition()

# #define a function to display a message "Hello Your name"
# def hello():
#      s=input('enter your name')
#      print('hello '+s)

# hello()

# #define a function to print the factorial of a number

# def fact():
#      num=int(input('enter the num'))
#      fact=1
#      for i in range(1,num+1):
#           fact*=i
#      print('factorial:',fact)     

# fact()
# #define a function to find the number of occurence of a particular character in a string
# def chcount():
#      s=input('enter the string')
     
#      for i in s:
#           count=0
#           for j in s:
#                if i==j:
#                      count+=1
#           print(i,count)

# chcount()


# def ccount():
#      s=input('enter the string')
#      n=input('enter the chr')
#      for i in s:
#           count=0
#           if i==n:
#               count+=1
#           print(i,count)

# ccount()
# #define a function to print the sum of elements in a  list l=[89,45,67,12]

# def sums():
#      l=[89,45,67,12]
#      sum=0
#      for i in l:
#           sum+=i
#      print(sum)

# sums()

#define an function to check whether prime or not


# def prime():
#      n=int(input('enter an number'))
#      for i in range(2,n):
#           if n%i==0:
#                print('not prime')
#                break
#      else:
#           print('prime')

# prime()

#define an function three argument (amount,rate,year) and simple intrest value


def intrest(amount,rate,year):
     i=(amount*rate*year)/100
     print('simple intrest:',i)




intrest(10000,5,5)



def intrest(amount,rate,year):
     i=(amount*rate*year)/100
     
     return i



 
intre= intrest(10000,5,5)
 
print(intre)

#define a function that takes 3 numbers and returns the product 0f 3 nums

def product(a,b,c):
     p=a*b*c
     return p

result= product(1,4,5)
print(result)

#define a function that takes a string and charatcter and returns the num of occurence of character in string


def freq(s,c):
     count=0
     for i in s:
          if i==c:
              count+=1
     return count

result = freq('sreejith','e')

print(result)