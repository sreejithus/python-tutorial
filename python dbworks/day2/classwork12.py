 #1.Create a table named students to store student information.
# Table: students
# Column Name
# Data Type
# Description
#
# student_id
# INT (Primary Key)
# Unique student ID
#
# name
# VARCHAR(100)
# Name of the student
#
# age
# INT
# Age of the student
#
# gender
# VARCHAR(10)
# Gender
#
# course
# VARCHAR(100)
# Enrolled course
#
# marks
# INT
# Marks obtained
#
# city
# VARCHAR(100)
# City of the student
#
#




import sqlite3


con=sqlite3.connect('Students.db')



con.execute("""create table if not exists students(
                 student_id int primary key,
                 name varchar(100),
                 age int,
                 gender varchar(30),
                 course varchar(100),
                 marks int,
                 city varchar(100))"""
)

print('table created')


# con.execute ("""insert into students(student_id,name,age,gender,course,marks,city)
#                values (101,"sreejith",21,"male","cse",90,'ekm'),
#                (102,"joyal",22,"male","ece",45,'tvm'),
#                (103,"abin",23,"male","cse",67,'tvm'),
#                 (104,"sreeraj",21,"male","cse",42,'kochi'),
#                (105,"geethul",21,"male","eee",76,'kochi')""")
#con.commit()






 #Display all records from the students table.

print((con.execute('select * from students')).fetchall())

# Display name, course, and marks for all students.

print((con.execute('select name,course,marks from students')).fetchall())


# Display names and marks of students who scored more than 80.

print((con.execute('select name,marks from students where marks > 80')).fetchall())

# Display all details of students enrolled in Computer Science.

print((con.execute('select * from students where course ="cse"')).fetchall())

# Display names, ages, and cities of students whose age is between 18 and 22.


print((con.execute('select name,age,city from students where age between 18 and 22')).fetchall())


# # Display names, marks, and courses of students from Kochi, sorted by marks in descending order.


print((con.execute('select name,marks,course from students where city = "kochi" order by marks desc')).fetchall())


# Insert a new record into the students table.

# con.execute("insert into students values  (106,'john',21,'male','ece',79,'kochi')")
# con.commit()
# # Update marks of all students who scored below 50 by adding 5 bonus marks.

con.execute("update students set marks= marks+5 where marks < 50")
con.commit()


# # Delete all student records where marks are less than 35.


con.execute('delete from students  where marks < 35')
con.commit()