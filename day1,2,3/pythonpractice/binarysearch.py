l1=list(map(int,input('enter the sortedd list elements:').split()))
key=int(input('enter the search element'))

low=0
high=len(l1)-1


while(low<=high):
         mid=(low+high)//2
         if(l1[mid]==key):
                 print('Target in',mid)
                 break
         elif(l1[mid]>key):
                 high=mid-1
         else:
                 low=mid+1
else:
        print('element not found')