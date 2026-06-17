'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
============================================

'''

'''

Start with 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

then say coin 2
[0,1, 0, 1, 0, 1, 0, 1, 0, 1]

coin 3
[0,1, 1, 1, 0, 2, 0, 1, 2, 1]

'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = (amount+1)*[0]
        dp[0]=1

        for coin in coins:
            for i in range(1,amount+1):
                if i%coin==0:
                    dp[i]+=dp[i-coin]

        return dp[amount]



        # We iterate over the dp list, and every time we divide evenly we add the previous coin
        






















'''
Trick here is to use Dynamic Programming. Start from the smallest coin, and continue adding in the number of sub elements. 
Keep adding them, and you will eventually get to the correct sum

ie for 9, we have five, three, two, one


how many ways are there to make 4 with 2 and 1,
1+1+1+1
2+1+1
2+2
[1,0,0,0,0,0,0]

1
[1,1,1,1,1,1,1,1,1,1]
2
[1,2,1,3,1,4,1,5,1,6]
3
[1,2,2,3,1,4+2=6]

[3,4]

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        





'''

Naively, this looks like a division / mod question. 

Use the smallest denomination, see if that works.

Iterate through them. This almost seems like a factorial problem. 

Should we check if the coins fit into eachother? Or just iterate through them?

Naively, check mod values for each number, and check if the remainder will fit into any other number 

5%1 = 0
5%2 = 1
5//2=2

Begin by checking if each of the coins fit in straightforwardly 

what if you started with the largest value?

pop it off the end, check for each of the other coins -> leads to O(n**2)

amount%coin -> Check both the remainder and the coin itself

coin%smallerCoin

starting with the largest

11%10= 1

1 %.....1 = 0

10+1

10%5=0
10//5=2

target, remainder -> Need to check both, probably a recursive function? 

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

say amount is 9, we have 3 and 1, and 5

[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

adding 3
[1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]

'''




class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0]=1 # Accounts for the null case

        for coin in coins:
            for i in range(coin,amount+1):
                dp[i]+=dp[i-coin]




















class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def checkForSubDenominations(coin,leftoverBag):
            for leftOver in leftOverBag:
                if coin%leftOver==0

        for coin in coins:
            if amount %coin==0:
                