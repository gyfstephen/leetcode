# coding=utf-8
# https://leetcode-cn.com/problems/longest-common-prefix/


class Solution(object):
    def prefix(self, str1, str2):
        tmp = 0
        len_1 = len(str1)
        len_2 = len(str2)
        for i in range(0, min(len_1, len_2), 1):
            if str1[i] == str2[i]:
                tmp += 1
            else:
                break
        return str1[0: tmp]

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        prefix = self.prefix(strs[0], strs[1])
        if not prefix:
            return ''
        for i in range(2, len(strs), 1):
            prefix = self.prefix(prefix, strs[i])
            if not prefix:
                return ''
        return prefix
