


'''
I think with this question it helps to 
1. Double check definition of a* -> 0 or more of the proceeding element
2. Work through a single element

QUESTION:-



dp
a*b*c
aac

    0   a   *   b   *   c
0   T   F   T   F   T   F
a   F   T   
a   F
c   F

Need to come up with a set of rules, generate an nxm matrix, and go over those rules:
If i,j = True, and s[j]=p[i],i+1 then j+1=True
If p[i]=="*" yields either dp[j][i-1] or dp[j][i]




'''



class Solution:
    # Time: O(?)
    # Space: O(?)
    def is_match(self, s: str, p: str) -> bool:

        s_len = len(s)
        p_len = len(p)

        dp = [[False for i in p_len+1] for j in s_len+1]

        dp[0][0]=True

        for i in range(p_len):
            if s[i]=="*":
                dp[0][i+1]=True

        for j in range(s_len):
            for i in range(s_len):





        # TODO: Implement is_match
        return False
