class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
                    
        return dp[-1] if dp[-1] != float('inf') else -1
