a=input("enter word1")
b=input('enter word2')

def anargam(a,b):
     d1={}
     d2={}
     for i in a:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
     for c in b:
          if c in d2:
            d2[c]+=1
          else:
            d2[c]=1

     if d1==d2:
         print("it is anargm")
     else:
         print('it is not anargm')
                   

anargam(a,b)

