'''



Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:



'''

'''


'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        target_len= len(candidates)
        res = []

        def backtrack(path,i,remainder):

            if remainder ==0:
                res.append(path)
            
            j = i
            while j < target_len:
                candidate= candidates[j]

                if remainder - candidate <0:
                    break
                
                if j>i and candidate==candidates[j-1]:
                    j+=1
                    continue
                j+=1
                backtrack(path+[candidate],j,remainder-candidate)
        backtrack([],0,target)
        return res

























'''
Backtracking solution:-> Like pruning off a tree. 



'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        can_len=len(candidates)

        def backtracksol(goal,path,position):

            path_length=len(path)

            if goal==0:
                res.append(path)
            
            for i  in range(position,can_len):

                if i>0 and candidates[i]==candidates[i-1]:
                    continue

                val=candidates[i]
                if val <= goal:
                    backtracksol(goal-val,path+[val],i+1)
                else:
                    break



        backtracksol(target,[],0)
        return res

        































'''
Before we had something like a dp list, but instead of using a regular DP,
we used a dictionary of lists. 
before we could use element an infinite number of times, now we can only use it once.
How do we track that? Start with the largest element, and work down from the top instead of up from the bottom?
[10,1,2,7,6,1,5]
Sorted 
[1, 1, 2, 5, 6, 7, 10]
start:-

{ 
    0:[]
}

Let's start with one. Check if i-value is in dict. If it is, add our value and continue

{ 
    0:[]
    1:[1]
}

Next one:-
{ 
    0:[]
    1:[[1],[1]]
    2:[1,1]
}
next one:-
{ 
    0:[[]]
    1:[[1],[1]]
    2:[[1,1],2]]
    3:[[1,2],[1,2]]
    4:[[1,1,2]]
}

Ok I think we got it! 

'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        l_dict = {0:[[]]}
        candidates.sort()

        for candidate in candidates:
            i = target
            while i>=0:
                if (i-candidate) in l_dict:
                    if i in l_dict:
                        current_l_dict=l_dict[i]
                    else:
                        current_l_dict=[]
                    for l_val in l_dict[i-candidate]:
                        current_l_dict.append(l_val+[candidate])

                    l_dict[i]=current_l_dict

                i-=1
        return l_dict[target]
            



