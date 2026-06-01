'''
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
-----------------------------------------------------


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
'''
'''
Create a set, add and remove chars from the set as you progress


'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set()

        left =0
        right=0
        maxCharLen=0
        maxChar=""

        while right <len(s):
            if s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            right+=1
            charLen=right-left
            if charLen>maxCharLen:
                maxChar=s[left:right+1]
                maxCharLen=charLen
        
        return maxChar



















'''
Trick here is to iterate over, keep track of the letters in the set, gradually pop ones out as they get reappear



'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set()
        right = left = maxSubLength=0

        longest_substring=''
        while right<len(s):
            right+=1
            char = s[right]
            while char in char_set:
                char_set.remove(s[left])
                left+=1
            
            char_set.add(s)
            subLength=right-left
            return maxSubLength










'''

SOLUTION ATTEMPT 3
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letSet = set()
        len_s=len(s)
        current_length=0
        leftPointer=0
        max_length=0

        for i in range(len_s):
            current_length+=1
            while s[i] in letSet:
                letSet.remove(s[leftPointer])
                current_length-=1
                leftPointer+=1
            letSet.add(s[i])
            max_length=max(current_length,max_length)
        
        return(max_length)

            









'''

Naively could generate a set at each point, and iterate through. 

At position 1, {a,b,c}
position 2,{b,c,a}
position 3,{c,a,b}
etc

n*n efficiency, n*n space use (one set at every line)

Is there other string manipulation techniques we can use? or can we use the strings look up, maybe store the locations in some sort of a dictionary and look them up?

ie for 1
a:[0,3]
b:[1,4,6,7]
c:[2,5]

Cant quite get it. Writing up naive soln
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        numSet = set()
        len_s=len(s)
        maxLen=0

        l=0
        r=0
        while r in range(len_s):
            j=0
            val = s[r]

            while s[r] in numSet:
                if i+j ==maxLen-1:
                    break
                numSet.remove(s[i+j])
                currentLen-=1



















































class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s=len(s)


        testSet=dict()

        currentMax=0
        totalMax=0
        j=0
        for i in range(len_s):
            if s[i] in testSet:
                j=testSet[s[i]]+1
                currentMax=i-j+1
                testSet[s[i]]=i
            else:
                testSet[s[i]]=i
                currentMax+=1
            if currentMax>totalMax:
                totalMax=currentMax
        return totalMax

