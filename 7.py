# coding=utf-8
# https://leetcode-cn.com/problems/reverse-integer/


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        sign = ''
        if x[0] == '-':
            sign = '-'
            int_part = x[1:]
        else:
            int_part = x
        ans = int(sign + int_part[::-1])
        if ans > 2 ** 31 - 1 or ans < -2 ** 31:
            return 0
        else:
            return ans
