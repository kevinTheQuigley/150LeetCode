'''
I think it will be some trick by evaluating each value seperately, then circling around with the final value


[1,-2,3,-2]
[1,1,3,3]

store the max value 



'''

class Solution():
    def maxSubarraySumCircular(self, nums):
        if len(nums)<1:
            return None
        
        maxVal = nums[0]
        if len(nums)==1:
            return maxVal


        i = 0
        cycle = True
        while i < len(nums)-1:
            i+=1
            if nums[i]+nums[i-1]<nums[i]:
                cycle =False
            nums[i] = max(nums[i]+nums[i-1],nums[i])
            maxVal = max(maxVal,nums[i])

        nums[0]=max(nums[i]+nums[0],nums[0])
        if cycle:
            return maxVal
        else:
            maxVal = max(nums[0],maxVal)

        print(nums)
        return maxVal

        


mySolution = Solution()


val = mySolution.maxSubarraySumCircular([1,-2,3,-2])
print("Should be 3, evaluates to",val)


val = mySolution.maxSubarraySumCircular([5,-3,5])
print("Should be 10, evaluates to",val)


val = mySolution.maxSubarraySumCircular( [-3,-2,-3])
print("Should be -2, evaluates to",val)