

for i in range(1,4):
    for j in range(1,4):
        print(i,j,end=' ')
    print('\n')



for i in range(1,4):
    for j in range(1,4):
        print(i,end=' ')
    print('\n')



for i in range(1,4):
    for j in range(1,4):
        print(j,end=' ')
    print('\n')


for i in range(10):
     for j in range(1,i+1):
          print(j,end=' ')
     print('\n')

l=['kelly','emy','alan']

for i in l:
     for j in range(3):
          print(i)



num=[1,2,3]
qns=['what','when','why']


for i in num:
     print(i)
     for j in qns:
         
         print(j,end=' ')
     print('\n')


l=[[1,2,3,4],[5,6,7,8]]

for i in l:
    print(i)
    for j in i:
        print(j)



l=[{'id':101,'name':'arun','age':23},
   {'id':102,'name':'amal','age':24},
   {'id':103,'name':'anu','age':22}]


for i in l:
    for j in i.values():
         print(j)