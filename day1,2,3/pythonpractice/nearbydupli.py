nums = [1, 2, 3, 1]
k = 2

seen={}
for i in range(len(nums)):
     num1=nums[i]
     if num1 in seen:
        if i-seen[num1]<=k:
            print(num1)
     
     seen[num1]=i