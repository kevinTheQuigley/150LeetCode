"""
This definitely looks like some kind of funky DFS algorithm. 

Start with a single character, then search if the next character is close to it.
If it is, append the character to a list of the current characters that are being used
Move to the next character. 

How should we handle the movement? 
We can go i-1,j i+1,j etc

How do we handle avoiding going backwards?
We could add the currently used positions to a set. When looking at where we can go next, we check the set. 

Do we need to construct any classes?
could use a trie
class Trie():
    def __init__(self):
        self.children={}
        self.is_word=False

But this may not be necessary -> There isn't the same split to get to the end and were not doing repeated queries






"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_col=len(board[0])
        len_row=len(board)

        def dfs(board,position,word):
            
            char = word[0]
            word = word[1:]
            (row,col)=position

            if row <0 or row>=len_row or col <0 or col >=len_col:
                return False
            position_char = board[row][col]

            if char !=position_char:
                return False
            board[row][col]=""

            if len(word)==0:
                return True

            res = bool    
            res= dfs(board,(row+1,col),word) or  dfs(board,(row-1,col),word) or  dfs(board,(row,col+1),word)  or  dfs(board,(row,col-1),word) 
            board[row][col]=position_char
            return res
        
        for row in range(len_row):
            for col in range(len_col):
                if dfs(board,(row,col),word):
                    return True
        return False
        



        


































class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        i_len = len(board[0])
        j_len = len(board)
        checkedSet = set()
        for i in range(i_len):
            checkedSet.add((i,-1))
            checkedSet.add((i,j_len))
        for j in range(j_len):
            checkedSet.add((-1,j))
            checkedSet.add((i_len,j))

        def dfs(word:float,position:tuple,checked:set):
            (i,j)=position
            checked.add(position)
            char = word[0]
            res = False

            if board[j][i] == char:
                if len(word)==1:
                    print("True on",i,j)
                    return True
                potential_positions=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                for potential_position in potential_positions:
                    if not potential_position in checked:
                        res += dfs(word[1:],potential_position,checked)
                return res
            else:
                print("False on",i,j)
                return False

        

        for j in range(j_len):
            for i in range(i_len):
                if dfs(word,(i,j),checkedSet):
                    return True
                print("checking ",i,j)
        return False


