'''
class Solution:
    # Time: O(?)
    # Space: O(?)
    def rotate(self, matrix: list[list[int]]) -> None:
        # TODO: Implement rotate
        pass


        
How to rotate the matrix in place? 
All of the solutions coming into my head involve allocating a second matrix.

Could I use some kind of parallel processing? I could use a stack? 

I could order the stack in the order we expect the answer. CHEEKY! 




'''


class Solution:
    # Time: O(?)
    # Space: O(?)
    def rotate(self, matrix: list[list[int]]) -> None:

        if matrix ==[[]]:
            return matrix

        # Using two for loops, and a last for loop (O(n*n))
        n = len(matrix)
        s = []

        for j in range(0,n):
            for i in range(n-1,-1,-1):
                s.append(matrix[i][j])

        for i in range(len(s)):
            matrix[i//n][i%n] = s[i]

        return matrix

