class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp stores num of coins reqd
        dp=[amount+1]*(amount+1)
        dp[0]=0
        # range is (i,j-1) , so taking amount+1
        for numberBoundedByAmount in range(1,amount+1):
            for coin in coins:
                if numberBoundedByAmount-coin>=0:
                    dp[numberBoundedByAmount]=min(dp[numberBoundedByAmount],dp[numberBoundedByAmount-coin]+1)
        return dp[amount] if dp[amount]!=amount+1 else -1 
    
    #t(n)=O(n*amount)
    #s(n)=O(n)