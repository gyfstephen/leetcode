# coding=utf-8
# https://leetcode-cn.com/problems/palindrome-number/


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            x = str(x)
            for i in range(0, len(x) / 2, 1):
                if x[i] != x[len(x) - i - 1]:
                    return False
            return True
