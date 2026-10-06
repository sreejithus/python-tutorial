#define an class book with following details

# data members
# book name
#authorid
#bookid
#authorname
#price
#booktitle
#methods-> getautherid(),getauthorname(),getbooktitle(),getprice(),setauthorname()
#setbooktitle(),setprice()


class book:

      def __init__ (self):
            self.bookname= input('enter the bookname')
            self.authorid= input('enter the authorid')
            self.bookid= input('enter the bookid')
            self.authorname= input('enter the authorname')
            self.price= int(input('enter the price'))
            self.booktitle= input('enter the booktitle')

      def getautherid(self):
            return self.authorid
      def getauthorname(self):
            return self.authorname
      def getbootitle(self):
            return self.booktitle
      def getprice(self):
            return  self.price
      def setauthorname(self) :
            newauthorname=input('enter new author name')
            self.authorname=newauthorname
            print("updated authorname is ",self.getauthorname())
      def setbootitle(self):
            newbooktitle=input('enter the new booktitle')
            self.booktitle=newbooktitle
            self.getbootitle()
            print("updated boootitle",self.getbootitle())
      def setprice(self):
            newprice=int(input('enter the new price'))
            self.price=newprice
            self.getprice()
            print("updated price is",self.getprice())




b1=book()
print(" authorid is",b1.getautherid())

b1.setauthorname()
b1.setbootitle()
b1.setprice()
