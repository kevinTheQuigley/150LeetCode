'''

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
'''

'''

This looks a little bit like a stack, or a backtracking problem. 

Maybe the two of them combined.

Pass a value indicating the number of positive parenthesis currently being used, 
and the number of parentheses which can be used.
A funciton then calls itself with both the closed and open parenthesis in the stack.



'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        returnList= []

        def generateParentheses(positivity,parenthesesLeft,currentString):
            
            if positivity >0:
                # Positivity indicates the number of open parentheses already used
                # Parenthesesleft indicates the number of open parethenses not used
                generateParentheses(positivity-1,parenthesesLeft,currentString+")")
            if parenthesesLeft>0:
                generateParentheses(positivity+1,parenthesesLeft-1,currentString+"(")
            
            if positivity==0 and parenthesesLeft==0:
                returnList.append(currentString)
        
        generateParentheses(0,n,"")

        return returnList


