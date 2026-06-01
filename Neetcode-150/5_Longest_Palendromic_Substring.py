'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

'''

'''
use two pointers and a function which begins at a point which is passed in 

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s=len(s)
        
        def checkPalinString(l:int,r:int)->str:
            
            while (l>=0 and r<len_s) and s[l]==s[r]:
                l-=1
                r+=1
            
            return s[l+1:r]

        maxPal='' 
        for i in range(len_s):
            st1=checkPalinString(i,i)
            st2=checkPalinString(i,i+1)

            if len(st1)>len(maxPal):
                maxPal=st1
            if len(st2)>len(maxPal):
                maxPal=st2

        return maxPal



                





'''
create a function which will return the longest palindromic subscring using left and right of a value

Use a for loop to check over every letter, iterate in both directions. 
Pass the function two values, the current substring, and the two values seperately


'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find_palindrome(l,r):
            while l>=0 and r>len(s) and s[l]==s[r]:

                s-=1
                r+=1
            return s[l:r+1]
        maxPal=0
        returnPal = []
        for i in range(len(s)):
            pal1 = find_palindrome(i,i)
            pal2 = find_palindrome(i,i+1)
            if len(pal1)>maxPal:
                maxPal=len(pal1)
                returnPal=pal1

            if len(pal2)>maxPal:
                maxPal=len(pal2)
                returnPal=pal2
        return returnPal



        







'''


Naively I think the trick is to iterate over the list at every point and 
check the values before and after the pointer.

First we check 0, then check 1.
We will need to check for even and odd palindromes. (ie if 3,4 are the same, iterate over the subsequent values)


'''



class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s=len(s)

        def checkPalinDrome(l:int,r:int) -> str:

            while l>=0 and r<len_s and s[l]==s[r]:
                left-=1
                right+=1
            return s[left+1:right]
        maxPalLen=0
        for i in range(len_s):
            pal1=checkPalinDrome(i,i)
            pal2=checkPalinDrome(i,i+1)
            if len(pal1)>maxPalLen:
                maxPalLen=len(pal1)

        








'''
intervals = [[1,3],[5,8],[6,7],8]

ret = []
for item in intervals:

    if type(item)==list:
        ret.extend(item)
    else:
        ret.append(item)


for item in intervals:

    if type(item)==list:
        for subItem in item:
            ret.append(item)
    else:
        ret.append(item)


[subItem for item for subItem in intervals if type(item==list) else item]
intervalEasy=[[1,3],[5,8],[6,7]]


[list for interval in intervals if type(interval)==list]
'''











class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)

        def returnOddPalindrome(pos:int,s:str) -> str:
            pos =pos-1
            iterator=2

            while True:
                if  s[pos]!=s[pos+iterator]or s<0 or s >= len_s:
                    break
                s-=1
                iterator+=2
            return s[pos:pos+iterator]

        def returnEvenPalindrome(pos:int,s:str) -> str:
            iterator=1
            if s[pos]!=s[pos+iterator]:
                return []

            while True:
                if  s[pos]!=s[pos+iterator]or s<0 or s >= len_s:
                    break
                s-=1
                iterator+=2
            return s[pos:pos+iterator]


        for i in range(len_s):
            oddPalin=returnOddPalindrome(i,s)
            evenPalin=returnEvenPalindrome(i,s)

        