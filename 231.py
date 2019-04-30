# coding=utf-8
# https://leetcode-cn.com/problems/power-of-two/comments/


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        return self.isPowerOfTwo(n / 2) if n % 2 == 0 else False
