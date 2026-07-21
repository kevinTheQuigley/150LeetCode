'''

Visualising the problem

m-3,n-5

[0,0,0,0,0]
[0,0,0,0,0]
[0,0,0,0,0]

At every point, unless the robot is at the end,
it can go down or right. 

'''

class Solution:
    # Time: O(?)
    # Space: O(?)
    def unique_paths(self, m: int, n: int) -> int:
        global paths

        paths = 0
        def move_robot(row,col):
            global paths
            if row <m-1:
                move_robot(row+1,col)
            if col<n-1:
                move_robot(row,col+1)
            if row==m-1 and col ==n-1:
                paths+=1
        move_robot(0,0)

        return paths