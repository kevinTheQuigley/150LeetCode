'''


Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
     

'''

'''
Create an index to keep track of the status of each index. 
Could use a stack. 
Problem is when we  have combinations like "([)]"

Do we want three separete stacks? or should we load them on top of each other.

Could we use a dictionary?

paren_dict:{
    "{":0
    "}":0
    "(":0
    ")":0
    "[":0
    "]":0
}

increase the values for every open bracket 

paren_dict["{"]+=1
paren_dict["}"]-=1

we should never see the value go negative -> ie always above zero

the problem is how to handle this edge case:-

Input: s = "([)]"
+1,+1,-1,-1 -> it would pass...

What about using a stack. 
Add a close parenthesis to the stack for an open parenthesis.

paren_stack=list()
if "{":
    paren_stack.add"}"
if "}":
    val = paren_stack.pop()
    check equality...
    if it passes it works, else it fails.



'''


class Solution:
    def isValid(self, s: str) -> bool:
        parenStack = list()
        parenDict={
            "{":"}",
            "[":"]",
            "(":")"
        }

        while len(s)>0:
            p=s[0]
            s=s[1:]
            if p in "{[(":
                parenStack.append(parenDict[p])
            else:
                char = parenStack.pop()
                if char !=p:
                    return False
        if len(parenStack)==0:
            return True
        else:
            return False
        
