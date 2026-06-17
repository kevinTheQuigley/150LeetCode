'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


'''

'''
The usual, create a set and take one away from the list

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_set=dict()

        for i in range(len(nums)):
            if nums[i] in num_set:
                return [i,num_set[nums[i]]]
            num_set[(target-nums[i])]=i











'''


 


What happens if we take each number from the target?

9-2=7,
add 7 to list of hashes we are searching for, if it's not present, add the next target difference to the list of hashes. Continue

This reminds me of a hash map-type exercise. We iterate over the list, modifying it so that we can search for the target (relatively) easily


 '''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetDict : dict = dict()

        for i in range(len(nums)):
            if nums[i] in targetDict:
                return(i,targetDict[nums[i]])
            else:
                targetDict[target-nums[i]]=i




