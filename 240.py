# coding=utf-8
# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if not m:
            return False
        n = len(matrix[0])
        if not n:
            return False
        i, j = m - 1, 0
        while i > -1 and j < n:
            key = matrix[i][j]
            if key == target:
                return True
            elif key > target:
                i -= 1
            elif key < target:
                j += 1
        return False
