
import os
def fileread():
       filename = input('enter the filename')
       f1= open(filename,'r')
       print(f1.read())
       f1.close()


def filewrite():
       filename = input('enter the filename')
       f2= open(filename,'w')
       content = input('enter the contents to write')
       f2.write(content)
       f2.close()

def fileappend():
        filename = input('enter the filename to append')
        f2= open(filename,'a')
        content = input('enter the contents to append')
        f2.write(content)
        f2.close()

def filesearch():
               filename = input('enter the filename')
               f1= open(filename,'r')
               l= f1.read().split()
               f= input('enter the word to search')
               for i in l:
                       if f == i:
                               print('word is present')
                               break
               else:
                       print('word is not present')
               f1.close()




def fileremove():
       filename = input('enter the filename to remove')
       os.remove(filename)




while(True):

    print('choose the option')
    print(' 1.File read\n 2.File write\n 3.File append\n 4.File search\n 5.File Remove\n 6.Exit')
    ch = int(input('enter the choice:'))

    if ch ==1:
           fileread()
    elif ch == 2:
            filewrite()
    elif ch ==3:
            fileappend()
    elif ch == 4:
           filesearch()
    elif ch ==5:
           fileremove()
    elif ch ==6:
           exit()
    else:
           print('invalid choice')


