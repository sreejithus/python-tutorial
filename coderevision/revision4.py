


def sol(nums):
        repeated=missing=None
        for i in range(len(nums)-1):
                if nums[i+1]-nums[i] == 0:
                           repeated = nums[i]     
                elif nums[i+1]-nums[i] == 2:
                         missing = nums[i]+1
                        
                if repeated is not None and missing is not None :
                       print('sum:',repeated+missing)
                       break



sol([1,2,3,3,4,5,7])



