# coding=utf-8
# https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        tmp = list()
        for i in s:
            if i != ' ':
                tmp.append(i)
            else:
                while tmp:
                    ans = ans + tmp.pop()
                ans = ans + i
        while tmp:
            ans = ans + tmp.pop()
        return ans
