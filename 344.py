# coding=utf-8
# https://leetcode-cn.com/problems/reverse-string/comments/


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(0, len(s) / 2, 1):
            s[i], s[-1 - i] = s[-1 - i], s[i]
