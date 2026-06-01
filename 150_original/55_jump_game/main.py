class Solution(object):
    def canJump(self, nums):
        jump = nums[0]
        li = len(nums)
        i = 1
        while  jump >=0:
            #print(i,jump,li)
            jumpAlt= nums[i-1]
            if i >= li:
                return True
            if jump < jumpAlt:
                jump = jumpAlt 
            jump-=1
            i+=1
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
prices = [2,5,0,0]
prices = [2,0,0]
prices = [2,3,1,1,4]
prices = [3,2,1,0,4]
prices = [0,1] #False
prices = [0] #True

the_solution = Solution()
print(the_solution.canJump(prices)) 