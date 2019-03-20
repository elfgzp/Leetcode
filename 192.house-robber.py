#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# https://leetcode-cn.com/problems/house-robber/description/
#
# algorithms
# Easy (39.15%)
# Total Accepted:    19K
# Total Submissions: 48K
# Testcase Example:  '[1,2,3,1]'
#
# 
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
# 
# 示例 1:
# 
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
# 示例 2:
# 
# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
# 
# 
#


class Solution1:

    def rob(self, nums: List[int]) -> int:
        """
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        dp[2] = max(dp[0] + nums[2], dp[1])
        dp[3] = max(dp[1] + nums[3], dp[2])
        ...
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        
        example: [1,2,3,1]
        dp[0] = nums[0] = 1
        dp[1] = max(dp[0], nums[1]) = max(1, 2) = 2
        dp[2] = max(dp[0] + nums[2], dp[1]) = max(1 + 3, 2) = 4
        dp[3] = max(dp[1] + nums[3], dp[2]) = max(2 + 1, 4) = 4
        
        example: [2, 7, 9, 3, 1]
        dp[0] = nums[0] = 2
        dp[1] = max(dp[0], nums[1]) = max(2, 7) = 7
        dp[2] = max(dp[0] + nums[2], dp[1]) = max(2 + 9, 7) = 11
        dp[3] = max(dp[1] + nums[3], dp[2]) = max(7 + 3, 11) = 11
        dp[4] = max(dp[2] + nums[4], dp[3]) = max(11 + 1, 11) = 12
        
        example: [2, 1, 1, 2]
        dp[0] = nums[0] = 2
        dp[1] = max(dp[0], nums[1]) = max(2, 1) = 2
        dp[2] = max(dp[0] + nums[2], dp[1]) = max(2 + 1, 2) = 3
        dp[3] = max(dp[1] + nums[3], dp[2]) = max(2 + 2, 3) = 4
        
        """
        if not nums:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        
        dp = [nums[0], max(nums[0], nums[1])]
        
        for i in range(2, len(nums)):
            dp.append(max(dp[i - 2] + nums[i], dp[i - 1]))
        
        return dp[-1]

        
class Solution:

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        
        pre1, pre2 = nums[0], max(nums[0], nums[1])
        for num in nums[2:]:
            pre1, pre2 = pre2, max(pre1 + num, pre2)
        
        return pre2
        
        

