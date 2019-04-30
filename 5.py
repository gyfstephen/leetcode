# coding=utf-8
# https://leetcode-cn.com/problems/longest-palindromic-substring/


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s
        dp = [[False for x in range(0, len(s), 1)] for y in range(0, len(s), 1)]
        dp[0][0], max_len, max_str = True, 1, s[0]
        for j in range(0, len(s), 1):
            for i in range(0, j + 1, 1):
                if i == j:
                    dp[i][j] = True
                else:
                    if j - i < 2 and s[i] == s[j]:
                        dp[i][j] = True
                        if j - i + 1 > max_len:
                            max_len = j - i + 1
                            max_str = s[i: j + 1]
                    elif j - i >= 2 and s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if j - i + 1 > max_len:
                            max_len = j - i + 1
                            max_str = s[i: j + 1]
        return max_str
