# coding=utf-8
# https://leetcode-cn.com/problems/nim-game/submissions/


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4
