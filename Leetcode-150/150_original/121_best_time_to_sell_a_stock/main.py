class Solution(object):
    def maxProfit(self, prices):
        maxP = 0 
        for i in range(1,len(prices)):
            
            maxi = max([prices[-i] - x for x in prices[:-i]])
            if maxi >maxP:
                maxP = maxi
        return maxP



#prices = [7,6,4,3,1] 
prices = [7,1,5,3,6,4]

the_solution = Solution()

print(the_solution.maxProfit(prices))