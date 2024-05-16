"""
274. H-Index

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
"""


class Solution(object):
    def canJump(self, nums):
        jump = 0
        li = len(nums)
        for i in range(li):
            print(i,jump,li)
            if jump < nums[i]:
                jump = nums[i]
        if jump>= li:
            return True
        else:
            return False

#        if nums[0] ==0:
#            move = 0
#        else:
#            move = nums[0]-1
#        index = 0
#        le= len(nums)
#        atEnd =False
#        while atEnd ==False:
#            print(index,move,le)
#            index += move
#            if index >= le-1:
#                return True
#                atEnd=True
#            move = nums[index]
#            if move == 0:
#                return False
#                atEnd = True

#prices = [7,6,4,3,1] 
prices = [3,2,1,0,4]
prices = [2,3,1,1,4]
prices = [0]
prices = [2,5,0,0]
prices = [2,0,0]

the_solution = Solution()
print(the_solution.canJump(prices)) 