# coding=utf-8
# https://leetcode-cn.com/problems/spiral-matrix/


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = list()
        m = len(matrix)
        if not m:
            return ans
        n = len(matrix[0])
        if m == 1:
            return matrix[0]
        if n == 1:
            return [x[0] for x in matrix]
        # 多个方向遍历
        for i in range(0, max(m / 2, n / 2), 1):
            if i < m / 2:
                for j in range(i, n - 1 - i, 1):
                    ans.append(matrix[i][j])
            if i < n / 2:
                for j in range(i, m - i - 1, 1):
                    ans.append(matrix[j][n - 1 - i])
            if i < m / 2:
                for j in range(n - 1 - i, i, -1):
                    ans.append(matrix[m - i - 1][j])
            if i < n / 2:
                for j in range(m - i - 1, i, -1):
                    ans.append(matrix[j][i])
        # 行数不同且存在奇数行或列需要补数据
        if m / 2 < n / 2 and (n % 2 == 1 or m % 2 == 1):
            ans = ans + matrix[m / 2][m / 2: -m / 2 + 1]
        # 行数不同且存在奇数行或列需要补数据
        if n / 2 < m / 2 and (n % 2 == 1 or m % 2 == 1):
            for i in range(n / 2, m - n / 2):
                ans.append(matrix[i][n / 2])
        # 行数相同且为技术需要补中心
        if m == n and m % 2 == 1:
            ans.append(matrix[m / 2][n / 2])
        return ans
