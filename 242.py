# coding=utf-8
# https://leetcode-cn.com/problems/valid-anagram/


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        res = dict()
        for i in s:
            if i not in res:
                res[i] = 1
            else:
                res[i] = res[i] + 1
        for j in t:
            if j not in res:
                return False
            else:
                res[j] = res[j] - 1
                if res[j] == 0:
                    res.pop(j)
        if not res:
            return True
        else:
            return False
