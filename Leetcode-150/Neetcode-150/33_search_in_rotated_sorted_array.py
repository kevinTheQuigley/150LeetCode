'''

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

class Solution:
    def search(self, nums: List[int], target: int) -> int:

'''

'''
Should we try and binary for the lowest point of the array?

I think we can still use the fact that the list is (almost) sorted

maybe we can use three values to determine where we should search?

[4,5,6,7,0,1,2]
 *     m     *

Searching for zero, we know it's not between four and seven.
Must be between 7 and 2.

[11,0,1,2,3,4,5,6,7,8,9,10]

you either have 
nums[bl]> nums[br] -> unsorted side

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bl=0
        br=len(nums)-1

        while bl < br:
            m = (bl + br)//2

            if nums[m]==target:
                return m
            if nums[bl]>nums[m]:
                # This is the unsorted side, check the other side!
                if nums[m] < target <= nums[br]:
                    bl=m+1
                else:
                    br=m-1
            else:
                if nums[bl] <= target < nums[m]:
                    br=m-1
                else:
                    bl=m+1

        if nums[(bl + br)//2]==target:
            return (bl + br)//2
        else:
            return -1
