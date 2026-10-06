#define an class named Employee 
# 
# accept name,age,salary,designation,palce from the user 

#getsalary(),showpersonaldetails()
# create two obj and call the function



class Employee:
         def __init__(self):
                 self.empid =input('enter the empid')
                 self.name = input('enter your name')
                 self.age =int(input('enter your age'))
                 self.salary=int(input('enter your salary'))
                 self.designation =input('enter your designation')
                 self.place=input('enter your place')


         def showpersonaldetails(self):
                 print('Emp id',self.empid)
                 print('Name',self.name)
                 print("Age",self.age)  
                 print("designation",self.designation)
                 print("place",self.place)

         def getsalary(self):
                 print("emp id:",self.empid,"\nsalary:",self.salary)


e1= Employee()
e1.showpersonaldetails()
e1.getsalary()


e2= Employee()
e2.showpersonaldetails()
e2.getsalary()
