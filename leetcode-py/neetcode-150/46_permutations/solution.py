'''
class Solution:
    # Time: O(?)
    # Space: O(?)
    def permute(self, nums: list[int]) -> list[list[int]]:
        # TODO: Implement permute
        return []


        
Combinatorics -> first choose the first element, leave the remainder

[a] [b,c]

[b] [a,c]

[c] [a,b]

from a we have 

[a,b] [c]
[a,c] [b]


'''


class Solution:
    # Time: O(?)
    # Space: O(?)
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(path,remainder):
            if remainder==[]:
                res.append(path)

            for i in range(len(remainder)):
                backtrack(path+[remainder[i]],remainder[:i]+remainder[i+1:])

        backtrack([],nums)

        return res
