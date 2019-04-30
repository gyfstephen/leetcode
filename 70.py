# coding=utf-8
# https://leetcode-cn.com/problems/climbing-stairs/


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * n
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp[0], dp[1] = 1, 2
        for i in range(2, n, 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]
