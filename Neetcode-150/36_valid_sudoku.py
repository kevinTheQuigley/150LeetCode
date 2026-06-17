'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


'''

'''
I wonder if we can validate this in a single pass, using a series of sets.
Just need to decide when each one is getting called. 
Maybe use a dictionary of sets?

row_dict={1:set(),2:set()...}
col_dict={1:set(),2:set()...}
square_dict={1:set}A

square dict values

9,9 =9

1,1=1

9//3



'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Reattempt
        row_dict = {i:set() for i in range(9)}
        col_dict = {i:set() for i in range(9)}
        square_dict = {i:set() for i in range(9)}

        for i in range(9):
            for j in range(9):


                s_val= board[i][j]
                if s_val ==".":
                    continue
                else:

                    sq_val = i//3+(j//3)*3
                    check = s_val in row_dict[i] or s_val in col_dict[j] or s_val in square_dict[sq_val]

                    if check:
                        return False
                    else:
                        row_dict[i].add(s_val)
                        col_dict[j].add(s_val)
                        square_dict[sq_val].add(s_val)
        return True



























        row_dict={
            0:set(),
            1:set(),
            2:set(),
            3:set(),
            4:set(),
            5:set(),
            6:set(),
            7:set(),
            8:set(),
            }

        col_dict=row_dict.copy()
        square_dict=row_dict.copy()

        def checkDict(so_dict,i,j):
            # Checking rowDict i contains value j
            if so_dict[i].__contains__(j):
                return False
            else:
                so_dict[i].add(j)
                return True


        for i in range(9):
            for j in range(9):
                val = checkDict(row_dict,i,board[i][j]) and checkDict(col_dict,j,board[i][j]) and checkDict(square_dict,i%3+j//3,board[i][j])
                if val==False:
                    return False

        return True

