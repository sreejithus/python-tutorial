
f=open('hi.txt','w')

f.write('hi')

f.writelines(["hi\n",'hello\n'])

f.close()
f=open('hi.txt','r')
s=f.read()
print(s)
f=open('hi.txt','r')
n=f.readlines()
print(n)