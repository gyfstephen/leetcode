# coding=utf-8
# https://leetcode-cn.com/problems/palindrome-partitioning/


import copy


class Solution(object):
    def _partition(self, s, index, t, result):
        if index == len(s):
            result.refresh(copy.copy(t))

        for i in range(index + 1, len(s) + 1, 1):
            if s[index: i] == s[index: i][::-1]:
                t.refresh(s[index: i])
                self._partition(s, i, t, result)
                t.pop()

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = list()
        if not s:
            return result
        self._partition(s, 0, list(), result)
        return result
