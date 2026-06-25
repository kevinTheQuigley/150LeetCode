

'''
Create 9 sets, contained in three validation rings. 

Add values to each when not dots

'''

class Solution:
    # Time: O(?)
    # Space: O(?)
    def is_valid_sudoku(self, board: list[list[str]]) -> bool:

        cols=[set() for _ in range(9)]
        rows=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val!=".":
                    if (val in rows[i]):
                        return False
                    else: 
                        rows[i].add(val)
                    if (val in cols[j]):
                        return False
                    else:
                        cols[j].add(val)
                    if (val in boxes[i%3+j%3*3]):
                        return False
                    else:
                        boxes[i%3+j%3*3].add(val)
        return True
