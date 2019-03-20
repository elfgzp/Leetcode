#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (47.65%)
# Total Accepted:    33.8K
# Total Submissions: 69.5K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
#
#
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#
#
#


class Solution1:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_prices = len(prices)

        if len_prices <= 1:
            return 0

        dp = [0]
        min_price = prices[0]

        for i in range(1, len_prices):
            dp.append(max(dp[i - 1], prices[i] - min_price))
            if prices[i] < min_price:
                min_price = prices[i]

        return max(dp)


class Solution2:

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        dp = [0]
        min_price = prices[0]

        for i in range(1, len(prices)):
            dp.append(max(dp[i - 1], prices[i] - min_price))
            min_price = min(prices[i], min_price)

        return dp[-1]


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        res, min_price = 0, prices[0]
        for p in prices:
            res, min_price = max(res, p - min_price), min(p, min_price)

        return res


