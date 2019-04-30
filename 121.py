# coding=utf-8
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price, max_profit = 2 ** 32, 0
        for i in range(0, len(prices), 1):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit
