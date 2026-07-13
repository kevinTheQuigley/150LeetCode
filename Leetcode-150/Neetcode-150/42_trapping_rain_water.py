'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

'''

'''
I got a sneaky hint that this is a DP question.

We need to look at how much water each unit can contain, 
possibly by sweeping over the array twice.

In the trapped water question, We need to look at boundary values, and work backwards from the outside. 

This is different, as the water is excluded from certain gaps.

For every value we go across, 
we have a max_L and a max_R which decide the boundary at any given point.

Do we do this using two pointers? and reseting the left pointer to be at the next max every time a new max is reached? 
-> This could work, might need to do two sweeps




'''

class Solution:
    def trap(self, height: List[int]) -> int:

        he_len = len(height)

        L_dp=[0]*(he_len)
        R_dp=[0]*(he_len)
        i=0
        max_L=0
        max_R=0

        while i <he_len:
            i_val= height[i]

            if i<he_len-2:
                if max_L< i_val:
                    max_L=i_val

                L_dp[i+1]=max_L
            i+=1

        i=he_len-1

        while i >0:
            i_val= height[i]

            if i >1:
                if max_R <i_val:
                    max_R=i_val

                R_dp[i-1]=max_R
            i-=1
        i=1
        water = 0
        while i <he_len-1:
            val = min(L_dp[i],R_dp[i]) - height[i]
            water+= val if val>0 else 0
            i+=1

        return water

                




                







