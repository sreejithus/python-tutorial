#define an class named person accept name and age from the user 

#display the details by using show() method

# create an obj and call the function

class person:
      def __init__(self):
            self.name = input('enter your name')
            self.age = int(input('enter your age'))


      def show(self):
            print('name is',self.name,"age is",self.age)



p = person()
p.show()

p1 = person()
p1.show()
