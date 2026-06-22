'''

class Solution:
    # Time: O(?)
    # Space: O(?)
    def length_of_longest_substring(self, s: str) -> int:
        s_len=len(s)
        l=0
        r=0
        maxLength=0

        letter_set=set()

        while r < s_len:

            while s[r] in letter_set:
                letter_set.remove(s[l])
                l+=1
            letter_set.add(s[r])
            r+=1
            if (r-l)>maxLength:
                maxLength=r-l

            



        return maxLength
'''


