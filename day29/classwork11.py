
# # 1.Create a class named Movie with attributes moviename,year,language,director,rating
# # and methods display_details() and update_rating()


# class Movie:
#     def __init__(self):
#         self.moviename = input('enter the movie name: ')
#         self.year =input('enter the year the movie released: ')
#         self.language = input('enter the language of the movie')
#         self.director = input('enter the director name ')
#         self.rating = ''


#     def display_details(self):
#           print(f"Moviename: {self.moviename} year of release: {self.year} language: {self.language} director: {self.director}")
#           if self.rating =='':
#                print('not yet rated')
#           else:
#                print("movie rating",self.rating)

#     def update_rating(self):
#          self.rating = input('enter the new movie rating')



# m=Movie()
# m.display_details()
# m.update_rating()
# m.display_details()












# # 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
# #
# # Create a parent class Vehicle with the attributes brand, model, color, and year.
# # Add a method display() in the Vehicle class to display these details.
# # Create two child classes:
# # Car with an additional attribute mileage
# # Bike with an additional attribute cc
# # Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# # Create objects of both classes, accept input from the user, and display the details.
# #

# #
# # create an abstract class Shape with abstract methods get_area() and get_perimeter()
# # create two subclasses
# #  -Rectangle
# #  -Square
# #
# #  -Each class should calculate area() and perimeter() differently.



# class Vehicle:
#      def __init__(self):
#           self.brand=input('enter the brandname ')
#           self.model=input("enter the modelname")
#           self.color =input('enter the color:')
#           self.year = input('enter the  year ')

#      def display(self):
#           print(f"brandname:{self.brand} modelname:{self.model} color:{self.color} year :{self.year}")



# class Car(Vehicle):
#        def __init__(self):
#             super().__init__()
#             self.milage =input('enter the milage of car')
#        def display(self):
#             super().display()
#             print('milage : ',self.milage)

# class Bike(Vehicle):
#       def __init__(self):
#            super().__init__()
#            self.cc= input('enter the cc of bike')
#       def display(self):
#                   super().display()
#                   print('cc of bike : ',self.cc)





# C=Car()
# C.display()
# # B=Bike()
# # B.display()



# #
# ## Create an abstract class Employee with an abstract method calculate_salary()
# # create two subclasses
# # -FullTimeEmployee
# # -PartTimeEmployee
# # Each class should calculate salary differently.






# from abc import ABC, abstractmethod
#
# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass
#
# class FullTimeEmployee(Employee):
#     def _init_(self):
#         self.salary = 50000
#     def calculate_salary(self):
#         print("Salary:", self.salary)
#
# f=FullTimeEmployee()
# f.calculate_salary()
#
#
# class PartTimeEmployee(Employee):
#     def _init_(self):
#         self.hour=int(input("Enter Part  Time  Hour:"))
#         self.rate=int(input("Enter Part Time  Rate:"))
#     def calculate_salary(self):
#      print("Salary:",self.hour * self.rate)
#
#
# p=PartTimeEmployee()
# p.calculate_salary()















# #
# # create an abstract class Shape with abstract methods get_area() and get_perimeter()
# # create two subclasses
# #  -Rectangle
# #  -Square
# #
# #  -Each class should calculate area() and perimeter() differently.


# # class Shape:
# #       def get_area(self):
# #             pass
# #       def get_perimeter(self):
# #             pass

# # class Rectangle(Shape):
# #       def __init__(self):
# #             self.bredth =int(input('enter the bredth'))
# #             self.length =int(input('enter the lenght'))

# #       def get_area(self):
# #             print('Area : ',self.bredth*self.length)
# #       def get_perimeter(self):
# #             print('perimeter',2*(self.bredth)+( self.length))


# # class Square(Shape):
# #       def __init__(self):
         
# #             self.length =int(input('enter the lenght'))

# #       def get_area(self):
# #             print('Area : ',self.length*self.length)
# #       def get_perimeter(self):
# #             print('perimeter',4*( self.length))




# # r=Rectangle()
# # r.get_perimeter()
# # r.get_area()


# # s=Square()
# # s.get_area()
# # s.get_perimeter()


# # Create a Python program using Object-Oriented Programming (OOP) that includes the following:

# # • Class: Course

# # Attributes:

# # coursename

# # instructor

# # duration
# # Methods:
# # showcourse() → to display course details

# # • Subclass: Student (inherits from Course)
# # Additional attributes:
# # name
# # rollno
# # marks
# # Methods:
# # showstudent() → to display student details along with course details
# # get_result() → return "Pass" if marks ≥ 50, otherwise "Fail"
# # Create at least one object of the Student class
# # Display all details and result

# class Course:

#       def __init__(self):
#             self.coursename = input('enter the coursename: ')
#             self.instructor = input('enter the instructorname: ')
#             self.duration = input('enter the duration: ')

#       def showcourse(self):
#             print(f"Coursename: {self.coursename} Instructor: {self.instructor} duration: {self.duration}")

# class Student(Course):
#       def __init__(self):
#             super().__init__()
#             self.name = input('enter your name: ')
#             self.rollno = int(input('enter your rollno: '))
#             self.marks =int(input('enter your marks: '))

#       def showstudent(self):
#             super().showcourse()
#             print(f"Name: {self.name} Rollno: {self.rollno} Marks :{self.marks}")

#       def get_result(self): 
#             if self.marks >=50:
#                   print('Pass')
#             else:
#                   print('Fail')



# s=Student()
# s.showstudent()
# s.get_result()



# Create a Python program using Object-Oriented Programming (OOP) that includes a class called Employee with attributes such as id, name, age, designation, experience (in years), and salary. The class should include methods to display employee details and update the designation.
# It should also include a method to check promotion eligibility where an employee is eligible for promotion if experience is 5 years or more and age is above 30; otherwise, the employee is not eligible.
# Create at least one object of the Employee class, assign values directly, and display all the details along with the promotion eligibility result.


# class Employee:

#        def __init__(self,id,name,age,designation,experience,salary):
#             self.id = id
#             self.name = name
#             self.age = age
#             self.designation = designation
#             self.experience = experience
#             self.salary = salary

#        def  display_employee_details(self):

#              print(f" ID : {self.id} Name: {self.name} Age: {self.age} Designation: {self.designation} Experience: {self.experience} salary : {self.salary}")
#              self.check_promotion()
#        def update_designation(self):
             
#               self.designation = input('enter the new designation')

#        def check_promotion(self):
#             if self.experience>=5 and self.age >30:
#                   print('Eligible for Promotion')
#             else:
#                   print('Not Eligible for Promotion')


# e= Employee(1,"sreejith",31,"software engineer",6,50000)

# e.display_employee_details()

# e.update_designation()

# e.display_employee_details()