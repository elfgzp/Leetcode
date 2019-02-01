# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
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