class Solution:
    # Time: O(?)
    # Space: O(?)
    def length_of_longest_substring(self, s: str) -> int:

        # Two pointer solution
        (l,r)=(0,0)

        n = len(s)
        set1 = set()
        max_dist = 0

        while r<n:
            
            while s[r] in set1:
                set1.remove(s[l])
                l+=1
            set1.add(s[r])
            r+=1
            max_dist = max(max_dist,r-l)
        return max_dist
    


'''
    
    
### Example 1:

```
Input: s = "abcabcbb"
Output: 3
```
**Explanation:** The answer is "abc", with the length of 3.

### Example 2:

```
Input: s = "bbbbb"
Output: 1
```
**Explanation:** The answer is "b", with the length of 1.

### Example 3:

```
Input: s = "pwwkew"
Output: 3
```
**Explanation:** The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''