#single level

class person:
    def m1(self):
        print('m1 in parent classs')
    def m2(self):
        print('m2 in parent class')
class Student:
    def m3(self):
        print('m3 in child class')
    def m1(self):               #Redefine -completly modify/extend the functionality 
        super().m1()            #method overriding
        print('m1 in child class')