
if __name__ == '__main__':
    n=int(input())
    list1=[]
    for _ in range(n):
       
             name = input()
             score = float(input())
             list1.append([name,score])




list1.sort(key=lambda x:x[1])
d=dict(list1)
minimum=list1[0][1]
d1=d.values()
count=0
for i in d1:
       if i>minimum:
             secondlargest=list1[count][1]
             break
   
       count+=1


l2=[]
for i in d:
       if d[i]==secondlargest:
              l2.append(i)

l2.sort()

print(l2)