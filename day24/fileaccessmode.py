f1=open('hi.txt','r')

f2=open('names.txt','a')


for i in f1:
    f2.write(i)
f2.close()

f3=open('zomato.txt','a+')

f3.write('gf')

print(f3.read().split())

print(f3.tell())
f3.seek(0)

print(f3.read())

import os
os.remove('hi.txt')