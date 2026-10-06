

import mysql.connector


con = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "49456243",
    

)

c= con.cursor()


c.execute("create database if not exists mydb1")

c.execute('use mydb1')


c.execute('create table student (id int,name varchar(30))')



 