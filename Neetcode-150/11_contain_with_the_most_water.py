'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104


class Solution:
    def maxArea(self, height: List[int]) -> int:
        

'''


'''
For this solution we need to compute the maximum area. 
To do this we work backwards towards the middle, 
computing the area as the sum between minimum of the heights times the difference between them.
This is a list type problem


[1,8,6,2,5,4,8,3,7]

[8*7]


1-
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:

        l_h=len(height)

        l =0
        r = l_h-1

        maxArea = 0
        while l!=r:

            area = min(height[l],height[r])*(r-l)

            maxArea=max(area,maxArea) 

            if height[l]>height[r]:
                r-=1
            else:
                l+=1

        return maxArea












'''

If we start from having two pointers at either side, and gradually work each one in,
Starting with the lower value and working in, we can keep track of the largest area



'''







class Solution:
    def maxArea(self, height: List[int]) -> int:
        global height


        def computeArea(left: int,right: int)->int:
            h= min(height[left],height[right])
            area = (right-left)*h
            return area

        l = maxArea = 0
        r=len(height)-1        
        while l<r:
            area = computeArea(l,r)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            maxArea=max(area,maxArea)
        return maxArea

        


































##workings
'''
This kind of split of values going across an array looks kind of like dynamic programming??

Start at the first element, skip it I guess, move to the second, use a function that works backwards
Input: height = [1,8,6,2,5,4,8,3,7]

Start from the second and work backwards, max height. 

Need to keep track of the max height at each index, the further back the better. 

0 -> maxheight 1
1 -> maxHeight 8

heightMax Array, do we generate the following to make calculations easier?

[1,8,8]

1 - [8] - 1 -> backwards to 1 -> max 1x1

2 - [6] - 6  

could we use some kind of lookup to find the previous maxHeight? 
ie we at index 3 see the max height is 8 looking backwards. 
maxHeight may not even do it, as if the value is further out 


an array showing where each element hit its max further back 

-> I think this makes more sense. 

[1,2,2,2,2,2,2,2,2]




'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxHeightArray = []
        positional_array=[]
        currentMax = 0 

        for i in range(height):
            if height(i)>currentMax:

                for i in range (height(i)-currentMax):
                    positional_array.append(i)
                currentMax = height(i)
                positional_array

            maxHeightArray.append(i)

        maxArea = 0
        for i in range(height)-1:
            area = i*positional_array[height[i]]

            if area>self.maxArea:
                maxArea=area
        return maxArea




        


                
     