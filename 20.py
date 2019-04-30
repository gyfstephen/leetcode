# coding=utf-8
# https://leetcode-cn.com/problems/valid-parentheses/


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = {')': '(', '}': '{', ']': '['}
        stack = list()
        for i in s:
            if i in tmp.values():
                stack.append(i)
            if i in tmp.keys():
                if stack and stack[-1] == tmp[i]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
