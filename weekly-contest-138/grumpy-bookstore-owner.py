class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        default = 0
        length = len(customers)
        for i in range(length):
            if grumpy[i] == 0:
                default += customers[i]
        
        dp = [default] * length
        for i in range(X):
            if grumpy[i] == 1:
                dp[0] += customers[i]
        
        ans = dp[0]
        for i in range(1, length - X + 1):
            count = dp[i - 1]
            if grumpy[i - 1] == 1:
                count -= customers[i - 1]
            
            if grumpy[i + X - 1] == 1:
                count += customers[i + X - 1]
            
            dp[i] = count
            ans = max(ans, count)
        
        print(dp)
        return ans

