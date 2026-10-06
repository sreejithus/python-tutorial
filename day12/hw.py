# # #check whether a number is an armstrong number

# # n=int(input('enter the number'))

# # count=len(str(n))
# # sum=0
# # s=n
# # while(n>0):
# #      N=n%10
# #      sum+=N**count
# #      n=n//10

# # print(sum)
# # if sum==s:
# #      print('num is armstrong')
# # else :
# #      print('num is not armstrong')


# # #Check whether a number is an Armstrong number

# # #Given a list
# # l=[1,2,3,4]
# # l1=[]
# # # create a new list with squares of each element
# # for i in l:
# #      l1.append(i**2)




# # #Given a list
# # l2=[12,67,59,23]
# # #create a list with elements whose value is greater than 50.

# # l3=[]
#s1=set()
# # for i in l2:
# #      if i>50:
# #           l3.append(i)
  #           s1.add(i)

# # # create a new set with elements whose value is greater than 50

# # #Given a list 
# # list1=[1,2,3,4]
# # #create a new dictionary where keys are numbers and values are squares of each number
# # d={}
# # for i in list1:
# #      d[i]=i**2
    
# # print(d)
     
     

# # ##create a list of 5 random numbers

# # import random
# # li1=[]
# # for i in range(5):
# # #       li1.append(random.randint(0,10))

# new=[]
# for i in range(5):
#     n=int(input('enter the num'))
#     new.append(n)
# # print(li1)
# # # #Find the factors of a number


# n=int(input('enter an number'))

# r=n//2
#print(n)
# for i in range(1,r+1):
#       if n%i==0:
#             print(i)

# #find the fibinocci series

n=int(input('enter the range'))
if n == 1:
         print(0)
       
elif n==2:
         print(0)
         print(1)
else:
         print(0,end=' ')
   
         a=0
         b=1
         for i in range(2,n):
            
              
                 b=a+b
                 print(b,end=' ')
                 a,b=b,a

# num=int(input('enter an number'))
# s=str(num)
# l=len(s)
# for i in s:
#     sum+=int(i)**l

# if sum==num:
#     print('armstrong')

# else:
#     print('not armstrong')

# a=0
# b=1

# for i in range(1,10):
#          print(a)
#          a,b=b,a+b