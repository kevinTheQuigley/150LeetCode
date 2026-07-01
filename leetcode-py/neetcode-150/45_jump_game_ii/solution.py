'''
Greedy algorithm

at any point check what the furthest point you can get to is

Do I just use a while loop?

create a counter that will check what the minimum jumps to get to a point are?

[] -> return 0
[1] -> return 0
[1,1] -> return 1

0:{2}
1:{1,3}
2:{1,2}
0 :[0] -> Start at 0
1:[1] -> 
2:[1,2]
3:

'''


class Solution:
    # Time: O(?)
    # Space: O(?)
    def jump(self, nums: list[int]) -> int:
        # TODO: Implement jump - example nums = [2,3,1,1,4] Output: 2
        jumps=0
        furthest=0
        current_jump_max=0
        n = len(nums)

        for i in range(n-1):
            furthest = max(furthest,i+nums[i])

            if i == current_jump_max:
                jumps+=1
                current_jump_max = furthest
            
                if current_jump_max >=n-1:
                    break
        return jumps

            































'''
Imagining it like a sort of level indexing game

Use a stack to keep track of where you are for a given level,
use the indices available at that level to see where you can jump to next.

n = nums[i] -> this is the available positions

level = 1 -> this is the number of jumps that have taken place


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

'''