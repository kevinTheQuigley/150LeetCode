'''
take the first position [0,0]

iterate in either direction

[0,0] -> [0,1],[1,0]

first get m & n -> If either is less then three, return the list

-> start at [1,1] -> mark candidates with a placeholder (or create a m-2,n-2 square to keep track)
-> 
-> check each value from [1,1] to [m-1,n-1]

-> within the small square you have X,

A tile is a candidate for switching if it's surrounded on all sides 

-> becomes xcan 

[xcan,xcan,o] 
[x,x,x]
[x,xcan,x]

If we are marking the x's and o's inside the main matrix, we only need to make one pass

Internal board keeps track of Xcandidates. These can be switched back. 
Allow a value to switch if the following values are possibilities. Switch it back if they are no longer valid

ie 

X X X 
X O O
X O X 

becomes
X X X
X C O
X O X

check the next O, now invalid again:-
X X X
X O O
X O X

//---------------------- ONLINE METHOD -----------------//
go around the exterior of the square using a function that relabels O's that touch O's as C's. 
The function should be recursively called on a given C-square to relabel the next O's as C's. 
Why it makes sense to use a recursive function - Before calling the function on the next cell, the value of the current cell is changed. 
This avoids an endless loop.

Another method seen adds the values to a deque
(i,j)
(3,4) -> Adds (3,3)
(4,3) -> ALSO adds (3,3)? -> No, there is too seperate loops, one over the edge elements, one of the deque of elements 
Similarly adds the cells, relablels them, then calls a recursive function on the elements

Why use a deque? would a list do?

X X X X
X O X X
X X O O
X X O X




On the following passes which are on the interior of the square, C's become O's and O's become X's

X X X X
X O X X
X X C C
X X C X

'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        daList=[]
        c="C"
        o="O"
        x="X"
        i_len = len(board)
        j_len = len(board[0])

        def inBounds(i,j):
            if ((i>=0) and (i <i_len)) and ((j>=0)and (j<j_len)):
                return True

        for i in range(len(board)):
            if board[i][0]==o:
                daList.append((i,0))
            if board[i][j_len-1]==o:
                daList.append((i,j_len-1))

        for j in range(len(board[0])):
            if board[0][j]==o:
                daList.append((0,j))
            if board[i_len-1][j]==o:
                daList.append((i_len-1,j))

        while daList:
            checkList= []
            (i,j) = daList.pop()
            board[i][j]=c
            checkList.extend([(i+1,j),(i-1,j),(i,j-1),(i,j+1)])

            for (ii,jj) in checkList:
                if inBounds(ii,jj):
                    if board[ii][jj]==o:
                        daList.append((ii,jj))

        for i in range(i_len):
            for j in range(j_len):
                if board[i][j]==o:
                    board[i][j]=x
                if board[i][j]==c:
                    board[i][j]=o

        return board

                







            

        """
        Do not return anything, modify board in-place instead.
        """
     