# coding=utf-8
# https://leetcode-cn.com/problems/valid-palindrome/


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        i, j = 0, len(s) - 1
        while i <= j:
            if not (s[i].isdigit() or s[i].isalpha()):
                i += 1
            elif not (s[j].isdigit() or s[j].isalpha()):
                j -= 1
            else:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
        return True
