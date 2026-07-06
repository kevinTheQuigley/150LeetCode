


'''
I think with this question it helps to 
1. Double check definition of a* -> 0 or more of the proceeding element
2. Work through a single element

QUESTION:-



dp
a*b*c

aac

Need to come up with a set of rules, generate an nxm matrix, and go over those rules
'''



class Solution:
    # Time: O(?)
    # Space: O(?)
    def is_match(self, s: str, p: str) -> bool:

        s_len = len(s)
        p_len = len(p)

        dp = [[False for i in p_len+1] for j in s_len+1]



        # TODO: Implement is_match
        return False
