
from collections import defaultdict 
"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1]
"""
class Solution(object):
    def jump(self, nums):
        #def def_value(): 
        #    return "Not Present"
        curPos = 0 
        le = len(nums)-1
        jumps = 0
        print("curPos,nextPos,jumps,le,maxJump")
        while curPos<le:
            maxJump = nums[curPos]
            nextPos = maxJump +curPos
            if nextPos ==le:
                return jumps+1
            elif nextPos >le:
                return jumps+1
            for j in range(nums[curPos]+1):
                if nums[curPos+j]+j>maxJump:
                    nextPos = curPos +j
                    maxJump = nums[curPos+j]+j
                print(curPos,nextPos,jumps,le,maxJump)
            jumps+=1
            curPos = nextPos

        return jumps

"""
class Solution(object):
    def canJump(self, nums):
        #def def_value(): 
        #    return "Not Present"
        curPos = 0
        nextPos = 0
        ln= len(nums)-1
        jumps = 1
        while curPos < ln:
            bn = nums[curPos] 
            print(nums)
            for i in range(nums[curPos]):
                if i+curPos>ln:
                    return(jumps)
                elif nums[i +curPos]+i>bn:
                    bn = nums[i+curPos]+i
                    nextPos = curPos+i
                    print(bn,nextPos,"elif")
            nums[curPos]-=nextPos
            jumps+=1
            print(curPos,jumps,nextPos)
            #curPos = nextPos
            curPos +=1


                
                
        return(jumps)

"""

#prices = [7,6,4,3,1] 
prices = [1,1,1,1]
prices = [2,3,0,1,4]
prices = [1]
prices = [2,3,1]
prices = [2,1]
prices = [2,3,0,1,4]
prices = [1,1,1]
the_solution = Solution()
print(the_solution.jump(prices)) 