# coding=utf-8
# https://leetcode-cn.com/problems/spiral-matrix-ii/


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[None] * n for i in range(0, n, 1)]
        if n % 2 != 0:
            ans[n / 2][n / 2] = n * n
        i, count = 0, 0
        while i < n:
            for j in range(i, n - i - 1, 1):
                count += 1
                ans[i][j] = count
            for j in range(i, n - i - 1, 1):
                count += 1
                ans[j][n - i - 1] = count
            for j in range(i, n - i - 1, 1):
                count += 1
                ans[n - i - 1][n - j - 1] = count
            for j in range(i, n - i - 1, 1):
                count += 1
                ans[n - j - 1][i] = count
            i += 1
        return ans
