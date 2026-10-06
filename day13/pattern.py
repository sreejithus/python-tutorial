for i in range(1,5):
    for j in range(1,5):
        print(i,end=' ')
    print()

for i in range(1,5):
    for j in range(1,5):
        print(j,end=' ')
    print()

for i in range(1,5):
    for j in range(1,5):
        print('*',end=' ')
    print()
for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
for i in range(1,5):
    for j in range(1,i+1):
        print('*',end=' ')
    print()


for i in range(1,5):
    for j in range(1,5):
             if i==j:
                   print(1,end=' ')
             else:
                  print(0,end=' ')
    print()

k=1
for i in range(1,5):
     for j in range(1,i+1):
              print(k,end=' ')
              k=k+1
     print()


for i in range(4,0,-1):
     for j in range(1,i+1):
              print('*',end=' ') 
     print()


k=2
for i in range(1,4):
     for j in range(1,i+1):
              print(k,end=' ')
              k=k+2
     print()

k=1
for i in range(1,4):
     for j in range(1,i+1):
              print(k,end=' ')
              k=k+2
     print()

for i in range(5,0,-1):
     for j in range(1,i+1):
              print(i,end=' ') 
     print()



for i in range(1,5):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

for i in range(1,5):
    for j in range(1,i+1):
         if j%2==0:
              print(0,end=' ')
         else:
             print(1,end= ' ')
         
    print()



for i in range(ord('A'),ord('D')+1):
          for j in range(ord('A'),i+1):
                  print(chr(i),end=' ')
          print()


k=ord('A')
for i in range(ord('A'),ord('D')+1):
          for j in range(ord('A'),i+1):
                  print(chr(k),end=' ')
                  k+=1
          print()



for i in range(ord('A'),ord('D')+1):
          for j in range(ord('A'),i+1):
                  print(chr(j),end=' ')
          print()

