

# #reverse the lines in a file

# f=open('marks.txt','r')



# s=[i.strip() for i in f.readlines()]
# s=s[::-1]
# f.close()
# f=open('marks.txt','w')
# for i in s:
#      f.write(i+'\n')





# # A file totalstudents.txt contains the names of all students in a class,
# # and a file passedstudents.txt contains the names of students who passed the exam.
# # Write a Python program to:
# # Read the names from both files.
# # Find the students who did not pass.
# # Write their names to a new file named failed_students.txt, one name per line.


# f1=open('totalstudents.txt','r')
# f2=open('passedstudents.txt','r')
# f3=open('failed_students.txt','w')


# for i in f1:
#      print(i)

# s=[i.strip() for i in f1.readlines()]
# a=[i.strip() for i in f2.readlines()]


# for i in s:
#     if i not in a:
#         f3.write(i+'\n')

# f1.close()
# f2.close()
# f3.close()

# # Two files, swiggy.txt and zomato.txt, contain the names of food items ordered from each platform.
# # Write a Python program to read words from swiggy.txt and zomato.txt, combine them, and count how many times each word appears. Store the result in a dictionary and print it

# with open('swiggy.txt','r') as f1:
#       s=[i.strip() for i in f1.readlines()]

# with open('zomato.txt','r') as f2:
#      a=[i.strip() for i in f2.readlines()]

# d={}
# c=[]
# c[:]=a+s

# for i in c:
#      if i in d:
#           d[i]+=1
#      else:
#           d[i]=1

# print(d)
