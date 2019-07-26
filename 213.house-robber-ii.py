class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
				# 这个条件可以不加
        if len(nums) <= 3:
            return max(nums)
        
				# 分别计算去头和去尾的数组最大值
        return max(self._rob(nums[:-1]), self._rob(nums[1:]))
    
    def _rob(self, nums):
        
        length = len(nums)
        
        if length <= 2:
            return max(nums)
        
        dp = [nums[0], max(nums[0], nums[1])]
        
        for i in range(2, length):
            dp.append(max(dp[i - 1], dp[i - 2] + nums[i]))
        
        return dp[-1]
