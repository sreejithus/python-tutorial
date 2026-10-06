

k=1
for i in range(1,5):
      for j in range(1,i+1):
             print(k**2 ,end=' ')
             k+=1
      print()


for i in range(1,6,2):
       for j in range(1,i+1):
             print(i,end=' ')
       print()



for i in range(1,6,2):
       for j in range(1,i+1):
              if j%2==0:
                     print('A',end=' ')
              else:
                     print(1,end=' ')
       print() 



k=3

for i in range(1,5):
       for p in range(1,k+1):
              print(' ',end=' ')
           
       k=k-1
       for j in  range(1,i+1):
         print('*',end='   ')
       print()


k=3

for i in range(1,5):
       for p in range(1,k+1):
              print(' ',end=' ')
           
       k=k-1
       for j in  range(1,i+1):
         print(5,end='   ')
       print()



k=0

for i in range(4,0,-1):
       for p in range(1,k+1):
              print(' ',end=' ')
           
       k=k+1
       for j in  range(i,0,-1):
         print('*',end='   ')
       print()
