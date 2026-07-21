'''

Hmm what is the trivial solution?

To have a greedy algorithm that computes at every step:-

find_next_step:
    if at end -> add to path
    otherwise take one step, call function, take two steps, call function

We need to create a way of caching the values-> this for sure is a dp problem



class Solution:
    # Time: O(?)
    # Space: O(?)
    def climb_stairs(self, n: int) -> int:
        # TODO: Implement climb_stairs
        return 1

'''
# This is the trivial solution
'''
class Solution:
    # Time: O(?)
    # Space: O(?)
    def climb_stairs(self, n: int) -> int:
        res = 0

        def take_next_step(i):
            nonlocal res

            if i == n-1:
                res+=1
            elif i ==n-2:
                take_next_step(i+1)
            else:
                take_next_step(i+1)
                take_next_step(i+2)
        
        

        take_next_step(0)
        return res
'''

# Creating the dynamic programming solution:-
class Solution:
    def climb_stairs(self, n: int) -> int:
        dp=(n+1)*[0]
        # Is the two ways to reach position n are (n-1 ) and (n-2)?
        # Manually compute first two values
        dp[0]=1
        dp[1]=2

        if n <3:
            return dp[n-1]

        for i in range(2,n):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n-1]