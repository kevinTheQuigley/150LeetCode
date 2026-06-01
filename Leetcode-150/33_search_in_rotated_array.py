'''
33. Search in Rotated Sorted Array
Attempted
Medium
Topics
premium lock icon
Companies
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

0
[4,5,6,7,0,1,2]  range is 4-6,7-2
 L   M,M+1   R

[4,5,6,7,0,1,2]  range is 4-6,7-2
       L,M,M+1,R

 [7,0,1,2,3,4,5,6]  range is 7-1,2-6
  L   M,M+1   R

 [7,0,1,2,3,4,5,6]  range is 7-1,2-6
  L,m,m+1,r

 Is it about which one has the bigger difference?


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right = len(nums)-1
        if right ==0:
            if nums[0]==target:
                return 0
            else:
                return -1
        middle=(left+right)//2

        while nums[middle]!=target:
            if nums[left] > nums[mid]:
                if nums[mid+1]<target<nums[right]

            elif nums[mid+1]
        

'''