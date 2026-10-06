


import sqlite3


con = sqlite3.connect('person.db')


con.execute('create table if not exists person (id int primary key,name varchar(30),age int)')



i = int(input('enter your id'))
n = input('enter your name')
a = int(input('enter your age'))


con.execute('insert into person(id,name,age) values(?,?,?)',(i,n,a))
con.commit()



i =int(input('enter id'))

e =con.execute('select * from person where id = ?',(i,))
print(e.fetchall())