
# f=open('hi.txt','r')

# s=f.readlines()
# print(len(s))


# f=open('hi.txt','r')

# s= f.read()

# print(len(s.split()))

# f=open('hi.txt','r')

#1write a program to read a text file and displays the number of lines in a file

#write a program to display the number of words in a file 


#write a program to update the second line in a file 

# f=open('hi.txt','r')

# s=f.readlines()

# def updatesecond(a):
#      s[1]=a


# updatesecond('sreejith')
# f.close()
# #f=open('hi.txt','w')
# #f.writelines(s)





#write a program to display the last 5 lines in a file 

# f=open('hi.txt','r')

# R= f.readlines()

# print(R[-5:])


#program to search a particular word in a file 

# f=open('hi.txt','r')

# S=f.read()

# def findword(a):
#       if a in S.split():
#             print('word is present in file')
#       else:
#             print('word is not present')

# findword('gdf')
# #find the number of letters,digits,and spaces in a file
# f.close()

f=open('hi.txt','r')

A=f.readlines()
dcount=0
scount=0
acount = 0
for i in A:
       for  j in i:
               if j.isdigit():
                     dcount+=1
               elif j.isalpha():
                     acount+=1
               elif j.isspace():
                     scount+=1

print(scount,acount,dcount)



print('python' in 'pythonworks')