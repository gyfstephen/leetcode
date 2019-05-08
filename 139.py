# coding=utf-8
# https://leetcode-cn.com/problems/word-break/


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        len_s = len(s)
        dp = [False] * (len_s + 1)
        dp[0] = True
        for i in range(1, len(s) + 1, 1):
            for word in wordDict:
                if i >= len(word) and dp[i - len(word)] and s[i - len(word): i] == word:
                    dp[i] = True
        return dp[-1]
