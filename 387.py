# coding=utf-8
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = dict()
        for i in range(0, len(s), 1):
            if s[i] not in res:
                res[s[i]] = i
            else:
                res[s[i]] = -1
        min_idx = -1
        for k, v in res.iteritems():
            if v >= 0:
                min_idx = min(min_idx, v) if min_idx != -1 else v
        return min_idx
