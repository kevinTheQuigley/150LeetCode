'''15. 3Sum
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
5,971,433/15.3M
Acceptance Rate
39.1%
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

'''

'''
I recall two ways of solving this. one way involves two pointers, and
 gradually iterating through them towards eachother.
The other would involve three pointers.

Assuming that the pointers iterate towards eachother. 
we could begin by adding the first pointer to all the other pointers. 
Then use a function that iterates over the remaining list


'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        n = len(nums)
        nums.sort()
        returnNums=[]
        nSet=set()

        for i in range(n):
            l=i+1
            r=n-1

            while l<n and l!=r:
                if nums[i]+nums[l]+nums[r]==0 and not (nums[i],nums[l],nums[r]) in nSet:
                    returnNums.append([nums[i],nums[l],nums[r]])
                    nSet.add((nums[i],nums[l],nums[r]) )
                    l+=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    l+=1
        return returnNums
            


     


'''
I think we'll need to apply one of the numbers to the remaining numbers in the list, and iterate over them every time.

It probably could be faster, we'll end up with an N**2 approach

We begin with [-1,0,1,2,-1,-4]

i = -1 -> apply this to all remaining numbers

[-1,0,2,-1,-4] -> Apply the rules of 'two Sum' to this -> Use a set of the remaining numbers.


j = 0 (from first list) -> apply to all remaining numbers and add to set
{1,2,-1,-4]}

check if the third value is a part of this set -> 1 and it is! We have a solution




Iterate over K


'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        len_nums=len(nums)
        for i in range(len_nums):
            nextNums = nums.copy()
            for j in range(nums[i:]):
                nextNums[j+i]+=nums[i]

            testDict= {}
            for j in range(nums[i+1:]):
                nextNums[j+i]+=nums[j+i]
                testDict[nextNums[j+i]]=j+i
            for j in range(nums[i+2]):
                if nums[j+i] in testSet:


            
