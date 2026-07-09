'''
With this solution we can have two pointers, 
and computer the maximum for any two points.

It all comes down to the height of the maximum
walls of the sides.

Start with two pointers on one side, 
and leave one of the pointers at the highest point
the other pointer works forward, the first pointer
catches up to it


Should we compute the maximum water at each index?
I think it could make sense! 






'''



class Solution:
    # Time: O(?)
    # Space: O(?)
    def trap(self, height: list[int]) -> int:
        h = len(height)
        l = 0
        r = 1

        # Compute the heighest value of the left, and the right going forwards 

        def find_water(current,left,right):
            water_height = min(height(left),height(right))
            water = water_height - height(current)
            if water >0:
                return water
        total_water = 0
        current = 1
        while current < h-2:


        # TODO: Implement trap
        return 0
