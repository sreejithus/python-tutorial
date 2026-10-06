

# class Person:
#          def __init__(self):
#                  self.name = input('enter your name')
#                  self.age = int(input('enter your age'))

#          def showdetails(self):
#                  print(f"Name : {self.name} Age: {self.age}")

# class Student(Person):
#            def __init__(self):
#                    super().__init__()
#                    self.rollno =int(input('enter your rollno'))

#            def showstdentdetails(self):
#                       super().showdetails()
#                       print(f"rollno : {self.rollno}")


# s=Student()
# s.showstdentdetails()


class Company:
        def __init__(self):
                self.companyname = input('enter your companyname :')

        def showdetails(self):
                print(f"Companyname: {self.companyname}",end='')


class Employee(Company) :
        def __init__(self):
                super().__init__()
                self.Empid = input('enter your empid')
                self.Designation = input('enter your designation')
                self.Salary = int(input('enter your salary'))
        def getsalary(self):
                print(f"empid: {self.Empid} and your salary is {self.Salary}")

        def Showemployeeedetails(self):
                super().showdetails()
                print(f" Empid: {self.Empid}  Designation: {self.Designation}  salary :{ self.Salary}")


C=Employee()

C.getsalary()
C.Showemployeeedetails()