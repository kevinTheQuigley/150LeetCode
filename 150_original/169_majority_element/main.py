#Header text 
from collections import defaultdict
class Solution(object):
    def majorityElement( self, nums):
        counterList = defaultdict(int)
        maxi = 0
        maxiRes = 0
        for i in nums:
            #if i in counterList.keys():
            counterList[i] +=1
            if counterList[i]> maxi:
                maxi = counterList[i]
                maxiRes= i
            #else:
            #    counterList[i]=1
            #    if counterList[i]> maxi:
            #        maxi = counterList[i]
            #        maxiRes= i
            
        return maxiRes

input_arrays = [[3,2,3],
                [6,5,5]]
#On the bottom    
the_solution = Solution()
for input_array in input_arrays:
    print(the_solution.majorityElement(input_array))