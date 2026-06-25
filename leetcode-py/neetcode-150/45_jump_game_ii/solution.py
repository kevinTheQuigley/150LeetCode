'''
Imagining it like a sort of level indexing game

Use a stack to keep track of where you are for a given level,
use the indices available at that level to see where you can jump to next.

n = nums[i] -> this is the available positions

level = 1 -> this is the number of jumps that have taken place

'''

class Solution:
    # Time: O(?)
    # Space: O(?)
    def jump(self, nums: list[int]) -> int:
        # TODO: Implement jump - example nums = [2,3,1,1,4] Output: 2
        n = len(nums)

        def checkLevel(position,level):
            r= range(position,position+nums[position]+1)
            if (n-1 in r):
                return level
            else:
                n_v = [checkLevel(i,level+1) for i in r]

                return min(n_v)





        return checkLevel(0,1)
