'''

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
Return a boolean indicating whether the matching covers the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        


'''
'''

This is a type of dynamic programming solution -> Key part I didn't understand before was about how a* can match "" or "a" or "aa"

example 
a*a*b
daab
    ""  a   *   a   *   b
""  1   0   1   0   1   0
d   0   0   1   0   1   0
a   0   0   1   1   1   0
a   0   0   1   1   1   0
b   0   0   0   0   0   1

if strings are equal 


'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        dp = [[False]*(len(p)+1)]*(len(s)+1)

        dp[0][0]=True
        for i in range(len(p)):
            if p[i]=="*":
                dp[0][i+1]=True
        
        for j in range(len(s)):
            for i in range(len(p)):




















'''
Using dynamic programing to track how the solution is going. 

Create an N+1 x Mx1 matrix
Initially iterate over the 0 values, checking for * as a value which can be skipped over.
Then check over every part of the matrix, setting empty values to 0


Need to visualise this as a dp problem - Take two example 
s="aa"
p="a"

    "" "a" "a"
""  T   T   F
"a" T   T   F

s="aa"
p="a*"

    "" "a" "a"
""  T   T   T
"a" T   T   T

s = "aab"  |  p = "c*a*b" 

i=col,j=row

    ""  "c" "*" "a" "*" "b"
""  T   F   T   F   T   F    
"a" F   F   F   T   T   F
"a" F   F   F   F   T   F
"b" F   

'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        (m,n)= (len(s),len(p))
        # M - s (target)
        # N - p (source)

        dp = [[False for _ in range(n+1)] for _ in range(m+1) ]

        for j in range(1,n):
            if p[j]=="*":
                dp[0][j+1] = dp[0][j-1]





















'''
In my memory, they create a way for the pattern to 'eat' the next letter. 

The challenge is (of course!) dealing with the star symbol

There is a way of staying ahead of the pattern, and eating the previous character. 
If the current symbol doesn't match and the next one is a star, skip this symbol.


If we get to the end of the pattern, at the same time as getting to the end of the string,
we have success.






'''



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Use i to track the position of the char in the string
        i = 0
        len_s=len(s)

        for letter in s:
            if s[i]==letter:
                i+=1
            elif s[i]==".":
                i+=1
            elif s[i]=="*":
                if i < len_s-1:
                    if s[i+1]==letter:
                        i=i+1
                        if i ==len_s-1:
                            return True
                        else:
                            i==i+2
                        

                elif i==len_s:
                    return True








'''


Looks like a string / set problem. Need to break the problem into chunks. 

Naive idea, just iterate over the list. if * appears, then we exclude all previous elements, if dot appears, 
just go over a single iterator. use a single value to detect if the value can match or not

just realised that the wildcard character makes it much harder, 
as you would need to iterate over the target multiple times if you detect that you are checking a wildcard.

I think I would begin by checking the pattern if there is wildcard characters present. 
If there is, we should check the string for characters adjacent to the wildcard string.
We should probably save a set of wildcard characters, ones that have wildcard before and ones that have wildcard after.
Processing dots is easier, as we just have is_fit=True

'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        leftWild=set()
        rightWild=set()

        len_s=len(s)
        len_p=len(p)

        for i in range(len_p):
            if s[i]=="*":
                if i>0:
                    leftWild.append(i-1)
                if i<i-1:
                    rightWild.append(i+1)

        isValidPattern=True 

        naiveValid=True

        for i in range(len_s):
            if 

            




       
