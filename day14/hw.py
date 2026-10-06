
for i in range(1,5):
    for j in range(1,i+1):
         print('*',end=' ')
    print()
#*
for i in range(3,0,-1):
    for j in range(i,0,-1):
         print('*',end=' ')
    print()





k=3

for i in range(1,4):
       for p in range(1,k+1):
              print(' ',end=' ')
           
       k=k-1
       for j in  range(1,i+1):
         print('*',end='   ')
       print()



k=0

for i in range(4,0,-1):
       for p in range(1,k+1):
              print(' ',end=' ')
           
       k=k+1
       for j in  range(i,0,-1):
         print('*',end='   ')
       print()


k=6

for i in range(2,9,2):
     for a in range(2):
         for p in range(1,k+1):
              print('',end=' ')
        
       
         for j in  range(1,i+1):
                  print('*',end='  ')
       
       
       
         
         print()
     k=k-2
