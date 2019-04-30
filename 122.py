# coding=utf-8
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, sell, profit = -1, -1, 0
        if len(prices) == 1: return profit
        for i in range(0, len(prices) - 1, 1):
            if buy < 0 and prices[i] < prices[i + 1]:
                buy = prices[i]
            if buy >= 0 and prices[i] > prices[i + 1]:
                sell = prices[i]
                profit = profit + sell - buy
                buy, sell = -1, -1
        if sell < 0 <= buy:
            if prices[i + 1] >= buy:
                profit = profit + prices[i + 1] - buy
        return profit
