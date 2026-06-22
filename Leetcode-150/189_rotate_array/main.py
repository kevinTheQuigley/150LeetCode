from collections import defaultdict
class Solution(object):
    def rotate(self, nums, k):
        lh= len(nums)
        ls = []
        for i in range(lh):
            ls.append(nums[(i+k+1)%(lh)])
        return ls

        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

input_array = [1,2,3,4,5,6,7]
#On the bottom    
the_solution = Solution()
    
print(the_solution.rotate(input_array,3))