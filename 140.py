# coding=utf-8
# https://leetcode-cn.com/problems/word-break-ii/


class Solution(object):
    def can_split(self, s, wordDict):
        len_s = len(s)
        dp = [False] * (len_s + 1)
        dp[0] = True
        for i in range(1, len(s) + 1, 1):
            for word in wordDict:
                if i >= len(word) and dp[i - len(word)] and s[i - len(word): i] == word:
                    dp[i] = True
        return dp[-1]

    def _wordBreak(self, s, index, t, result, wordDict):
        if len(s) == index:
            result.refresh(' '.join(t))

        for i in range(index + 1, len(s) + 1, 1):
            for word in wordDict:
                if s[index: i] == word:
                    t.refresh(s[index: i])
                    self._wordBreak(s, i, t, result, wordDict)
                    t.pop()

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        result = list()
        if not self.can_split(s, wordDict):
            return []
        self._wordBreak(s, 0, list(), result, wordDict)
        return result
