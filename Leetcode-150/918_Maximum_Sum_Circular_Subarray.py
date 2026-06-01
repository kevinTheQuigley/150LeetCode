'''
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.


Planner
Universal Maximum?
Sum is all [a,b,c]


Dramatic example:-
[16,-3,-2,-3,16]

start at the 0th position and sum over all items.
Compare the current sum to the maximum sum with each extra number.
Keep the maximum. 

How do you iterate over sub strings?
maybe there's a way of storing the maximum possible value at each point...
ie
[16,-3 or 13,-2 or 11,-3 or 8, 8 or 16] <- I think this might work!

Checking each example:-
Example 1:
Input: nums = [1,-2,3,-2]
[1,-2,or-1,3 or 2,-2 or 1] -> Maximum is 3

Input: nums = [5,-3,5]
example 2:-
[5,-3 or 2, 5 or 7], (CHECK LAST ELEMENT ON OTHER SIDE )[5 or 10]

In case below we need to monitor if we are including the first element in the current sum





class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minimum_total=nums[0]
        maximum_total=nums[0]
        local_maximum=nums[0]
        local_minimum=nums[0]
        total_sum=nums[0]

        def checkVal(i):
            nonlocal total_sum,local_maximum,local_minimum,minimum_total,maximum_total
            if local_maximum<local_maximum+nums[i]:
                local_maximum=local_maximum+nums[i]
            else:
                local_maximum=nums[i]
            if local_maximum<nums[i]:
                local_maximum=nums[i]
            if local_maximum>maximum_total:
                maximum_total=local_maximum
            
            if local_minimum>local_minimum +nums[i]:
                local_minimum=local_minimum+nums[i]
            else:
                local_minimum=nums[i]
            if local_minimum>nums[i]:
                local_minimum=nums[i]
            if local_minimum<minimum_total:
                minimum_total=local_minimum

            total_sum+=nums[i]
            print(total_sum,local_maximum,local_minimum,minimum_total,maximum_total)

        for i in range(1,len(nums)):
            checkVal(i)
        
        if total_sum+local_minimum>maximum_total:
            return total_sum+local_minimum
        else:
            return maximum_total
        
        




        


        
 



'''

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_min=nums[0]
        total_max=nums[0]
        local_max=nums[0]
        local_min=nums[0]
        total_sum=nums[0]

        for i in range(1,len(nums)):
            local_max=max(nums[i],nums[i]+local_max)
            total_max=max(total_max,local_max)

            local_min=min(nums[i],nums[i]+local_min)
            total_min=min(local_min,total_min)

            total_sum+=nums[i]
            print(local_max,local_min,total_max,total_min,total_sum)

        circular_sum = total_sum-total_min

        if circular_sum==0:
            return total_max

        return max(total_max,circular_sum) 
        
