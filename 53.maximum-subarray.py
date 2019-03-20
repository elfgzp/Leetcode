#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (42.41%)
# Total Accepted:    42.7K
# Total Submissions: 98.5K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#


class Solution1:
    
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        dp[0] = nums[0]
        dp[1] = max(nums[0] + nums[1] if nums[0] + nums[1] > 0 else nums[1], dp[0])
        dp[2] = max(nums[0] + ... + nums[2] if ... > 0 else nums[2], dp[1])
        ...
        dp[i] = max(nums[0] + ... + nums[i] if ... > 0 else nums[i], dp[i - 1])
        """
        if not nums:
            return 0

        dp = [nums[0]]
        sum_nums = 0

        for num in nums:
            sum_nums = 0 if sum_nums < 0 else sum_nums
            sum_nums += num

            dp.append(max(sum_nums, dp[-1]))
        
        return dp[-1]


class Solution:

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        sum_nums, max_sum = 0, nums[0]

        for num in nums:
            sum_nums = 0 if sum_nums < 0 else sum_nums
            sum_nums += num
            max_sum = max(sum_nums, max_sum)

        return max_sum
