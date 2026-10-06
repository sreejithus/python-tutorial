

import mysql.connector


con = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "49456243",
    

)

c= con.cursor()


c.execute("create database if not exists mydb1")

c.execute('use mydb1')


c.execute('create table if not exists employee(emp_id int primary key,name varchar(30),age int,salary int,gender varchar(20),place varchar(20))')

print('table created')


# c.execute("""insert into employee(emp_id,name,age,salary,gender,place) values (101,'sreejith',21,25000,'male','ekm'),(102,'arjun',28,35000,'male','cochin'),
#     (103,'neha',24,30000,'female','trivandrum'),
#     (104,'ranjith',30,45000,'male','kannur'),
#     (105,'meera',26,32000,'female','alappuzha'),
#     (106,'vijay',22,28000,'male','thrissur')
# """)



# con.commit()


c.execute('select * from employee')
data =c.fetchall()

print(data)



#read all the records with attribute name,age

c.execute('select name,age from employee where emp_id = 101')
data = c.fetchall()

print(data)




c.execute('select * from employee where name like "s%"')

print(c.fetchall())


c.execute('update employee set name ="sreejith us" where emp_id = 101' )

con.commit()



