s='programming'


l1=[]


for i in s:
    if i in l1:
        print("first-rep",i)
        break
    else:
        l1.append(i)