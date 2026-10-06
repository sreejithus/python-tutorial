import mysql.connector


con = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "49456243",
    

)

c= con.cursor()


c.execute("create database if not exists school")

c.execute('use school')



c.execute('create table  if not exists Student(roll_no int primary key,name varchar(50),age int,gender varchar(30),course varchar(30),mark int)')




# Create a database file school.db
#
# create a table Student with fields roll_no(pk),name,age,gender,course,mark
#
# write a menu driven code
#
#                     1.Insert Student details
#                     2.Read all student details
#                     3.search a student by rollno
#                     4.update the mark of a student
#                     5.Delete a student record
#                     6.Exit







def insert_record():
       rollno =  int(input('enter an rollno: '))
       name = input('enter the name: ')
       age = int(input('enter the age of student: '))
       gender =  input('enter the gender: ')
       course = input('enter the course')
       mark =  int(input('enter the mark: '))
       c.execute('insert into Student(roll_no,name,age,gender,course,mark) values (%s,%s,%s,%s,%s,%s)',(rollno,name,age,gender,course,mark ))
       con.commit()



def read_all_record():
     c.execute('select * from Student')
     print(c.fetchall())



def search_student():
     n =int(input('enter the rollno'))
     c.execute('select * from Student where roll_no = %s',(n,))
     k=c.fetchall()
     if k:
          print('student details available in db')
     else:
          print('student does not exist')
     


def update_mark():
          n =int(input('enter the rollno'))
          m= int(input('enter the updated mark:'))
          c.execute('select * from Student where roll_no = %s',(n,))
          k =c.fetchall()
          if k:
             c.execute('update Student set mark = %s where roll_no = %s',(m,n))
             print('update sucessfull')
          else:
               print('student does not exist')
     
def delete_student():
      n=int(input('enter the roll no to be delete: '))
      c.execute('select * from Student where roll_no = %s',(n,))
      k=c.fetchall()
      if k:
            c.execute('delete from Student where roll_no = %s',(n,)) 
            print('item deleted')   
      else:
          print('student does not exist')
while True:

    print('choose your operation')
    print('1.Insert Student Details')
    print('2.Read all student details')
    print("3.search a student by rollno")
    print('4.update the mark of a student')
    print(' 5.Delete a student record')
    print('6.Exit')
    ch = int(input('enter your choice: '))
    if ch == 1:
        insert_record()
    elif ch ==2:
        read_all_record()
    elif ch == 3:
         search_student()
    elif ch == 4:
          update_mark()
    elif ch == 5:
         delete_student()
    elif ch ==6:
          exit()
    else:
         print('invalid choice')



