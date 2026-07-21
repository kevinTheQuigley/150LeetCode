'''
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]



It's almost like having two pointers that have a maximum, 
and a minimum range. The range changes after they iterate over the list.

range begins 


i-> rows [0,n-1] (n - num rows)
j -> columns [0,m-1] -> Gets iterated over first 
[i][j]

always either going up or down one side or the other

while i_min<i_max and j_min<j_max:

The logic is tricky

0 -> n-2 , 0,n-1 -> 






'''

class Solution:
    # Time: O(?)
    # Space: O(?)
    def spiral_order(self, matrix: list[list[int]]) -> list[int]:

        i_min,j_min=0,0
        i_max,j_max = len(matrix)-1,len(matrix[0])-1
        res = []
        (i,j)=(0,0)
        while i_min<=i_max and j_min<=j_max:
            if j<=j_min:
                while j<j_max:
                    res.append(matrix[i][j])
                    j+=1
                i_min+=1

            if i<=i_min:
                while i <i_max:
                    res.append(matrix[i][j])
                    i+=1
                j_max-=1
            
            if j>=j_max:
                while j>j_min:
                    res.append(matrix[i][j])
                    j-=1
                i_max-=1

            if i >=i_max:
                while i>i_min:
                    res.append(matrix[i][j])
                    i-=1
                j_min+=1


        # TODO: Implement spiral_order
        return res
