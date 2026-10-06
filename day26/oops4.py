#define an class named Student with following details 
# 
# accept name,rollno,class,mark1,mark2,mark3  from the user 

#calculate(),calculate the total and average
#showdetails(),display the student details with average

# create two obj and call the function


class Student:
      def __init__(self):
            self.name=input('enter your name: ')
            self.rollno=int(input('enter your rollno: '))
            self.classname=input('enter your classname: ')
            self.mark1=int(input('enter your mark1: '))
            self.mark2=int(input('enter your mark2: '))
            self.mark3=int(input('enter your mark3: '))


      def calculate(self):
               total=self.mark1+self.mark2+self.mark3

               avgmark = total/3
               return avgmark

      def showdetails(self):
             print('Name: ',self.name)
             print('rollno: ',self.rollno)
             print('classname: ',self.classname)
             print("Average Mark :",self.calculate())



s1=Student()
s1.showdetails()

