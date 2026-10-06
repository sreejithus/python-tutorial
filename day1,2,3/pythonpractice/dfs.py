n=int(input('enter the number of edges'))

l1=[]
for i in range(n):
    s,a=(input('enter the connection').split())
    l1.append([s,a])

start=input("enter the start index")

d1=dict(l1)

print(d1)