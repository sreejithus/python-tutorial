
# # B.display()



# #
# ## Create an abstract class Employee with an abstract method calculate_salary()
# # create two subclasses
# # -FullTimeEmployee
# # -PartTimeEmployee
# # Each class should calculate salary differently.


# # class Employee:
# #       def calculate_salary(self):
# #             pass


# # class FulltimeEmployee:
# #        def calculate_




















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
