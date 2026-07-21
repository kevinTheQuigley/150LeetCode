class Solution:
    # Time: O(?)
    # Space: O(?)
    def can_jump(self, nums: list[int]) -> bool:
        # I think this is easier then jump game 2? Why is the number higher?
        # Compute how far you can go at each step, check if you can make it to the end
        # Begin by checking the maximum you can jump to, at each step.
        # If the current is ever greater then maximum, break and return False
        # If the end is reached, return true
        n = len(nums)
        if len(nums)==0:
            return True
        max_jump = nums[0]
        position = 0
        while position <n:
            if position >max_jump:
                return False
            else:
                max_jump= max(max_jump,nums[position]+position)
            position+=1


        return True
