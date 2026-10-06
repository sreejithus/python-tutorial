import json


#read

f=open('sample.json','r')

content = json.load(f)
print(content[0])

data =[
        {'name':'sreejith','age':21},
        {'name':'joyal','age':22}


]

f1=open('samples.json','w')
json.dump(data,f1)