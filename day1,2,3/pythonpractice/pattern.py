n=int(input('enter the no of lines'))


for i in range(1,n+1):
     for j in range(1,i+1):
             
             print(j,end=' ')
     print('\n')


for i in range(n+1,1,-1):
         for j in range(1,i):
                  print(j,end=' ')
         print('\n')


for i in range(1,n+1):
     while(n>0):
            print(' ')
            n=n//2
     for j in range(1,i+1):
            
            print(j,end=' ')
     print('\n')
