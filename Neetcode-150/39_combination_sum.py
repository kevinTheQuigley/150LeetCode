'''

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40




class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        '''

'''
This really reminds me of the coin change problem. 
I think it works in a similar way. 

We are looking at returning lists of combinations, which is different to before.

I do like the idea of a DP solution, but this is backtracking problem. 

I could save the combinations of each set of numbers in a numDict, and add the different combinations 

ie for 
[2,3,6,7], target = 7
[0,0,0,0,0,0,0]
[0,1,0,1,0,1,0], {0:[0],2:[2],4:[2,2],6:[2,2,2]}
[0,1,1,1,1,2,1], {0:[0],2:[2],3:[3],4:[2,2],5:[2,3],7:[2,2,3]}


'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        dp = [0]*(target+1)
        dp[0]=1

        numDict = {}

        for candidate in candidates:
            if candidate in numDict:
                numDict[candidate].append([candidate])
            else:
                numDict[candidate]=[[candidate]]
            for i in range(candidate,target):

                if (i - candidate) in numDict:
                    for subList in numDict[i-candidate]:
                        if i in numDict:
                            numDict[i].append(subList.extend(candidate))
                        else:
                            numDict[i] = [subList.extend(candidate)]

