import sqlite3

con = sqlite3.connect('company.db')

command = """create table if not exists employee(
                 emp_id int primary key,
                 name varchar(30),
                 age varchar(30),
                 place varchar(30),
                 gender varchar(30),
                 designation varchar(30),
                 salary int) """

con.execute(command)
# print('Table created')

# command = """insert into employee(emp_id,name,age,place,gender,designation,salary)
#               values (101,"sreejith",21,"kodungallur","male","tester",25000),
#               (102,"joyal",22,"tvm","male","developer",25000),
#               (103,"abin",23,"kottayam","male","tester",35000),
#               (104,"sreeraj",21,"kodungallur","male","devops enginner",45000),
#               (105,"geethul",21,"pathanamthitta","male","developer",35000)"""

# con.execute(command)
# con.commit()
# print('Values added')




# command = "select * from employee"


# e= con.execute(command)

# print(e.fetchall())

# e =con.execute('select * from employee where emp_id = 101')

# print(e.fetchall())

# e =con.execute('select name,age from employee where emp_id =101')

# print(e.fetchall())





# e= con.execute('select * from employee where age>=25 and salary<30000')

# print(e.fetchall())


# #read all employee records with emid other than 102


# e= con.execute('select * from employee where not(emp_id=102)')

# print(e.fetchall())

# #read all employee records with place ="ekm" or age<=25

# e =  con.execute('select * from employee where place = "kodungallur" or age<=25')

# print(e.fetchall())


# #employee records having salary between 20000 and 30000 (including 20000 and 30000)


# e = con.execute('select * from employee where salary between 20000 and 30000')
# print(e.fetchall())


# #employee records having age between 20 and 25 (return name,age)

# e= con.execute('select name,age from employee where age between 20 and 25')
# print(e.fetchall())


# #Like

# #employee name starting with letter "A"

# e = con.execute("select * from employee where  name like 'a%'")

# print(e.fetchall())

# #employee with 4 char starts with a

# e = con.execute("select * from employee where name like 'a___'")

# print(e.fetchall())



# #employeee record with place starting with "t"

# e = con.execute("select * from employee where place like 't%'")

# print(e.fetchall())



# e = con.execute("select * from employee where place like '__m'")

# print(e.fetchall())






# #employee record having age<25 and name starting with letter "a"

# e = con.execute("select * from employee where age<25 and name like 'a%' ") 

# print(e.fetchall())



# #employee records where having salary 50000 and 3 letter place name starting with "t"

# e =con.execute("select * from employee where salary = 25000 and place like 't__' ")


# print(e.fetchall())


#employee records having age = 30 or age = 23

#in
# e= con.execute('select * from employee where age in (23,30)')
# print(e.fetchall())



#orderby 

# e = con.execute('select * from employee order by place')
# print(e.fetchall())


# e= con.execute('select * from employee order by age desc')
# print(e.fetchall())



#distinct 

# e= con.execute('select distinct(place) from employee ')

# print(e.fetchall())



#updation 


con.execute("update employee  set name ='kiran',age=34 where emp_id = 102")

con.commit()



con.execute("delete  from employee where emp_id = 103")

con.commit()


