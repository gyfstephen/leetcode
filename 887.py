# coding=utf-8
# https://leetcode-cn.com/problems/super-egg-drop/comments/


class Solution(object):
    dp = None

    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        self.dp = [[None for col in range(N + 1)] for row in range(K + 1)]
        for i in range(1, N + 1, 1):
            self.dp[0][i] = 0
            self.dp[1][i] = i
        for i in range(1, K + 1, 1):
            self.dp[i][0] = 0
        return self.recursive(K, N)

    def recursive(self, K, N):
        if self.dp[K][N]:
            return self.dp[K][N]

        if N == 0 or N == 1 or K == 1:
            self.dp[K][N] = N
            return N

        min_count = N
        for i in range(1, N + 1, 1):
            count = max(self.recursive(K - 1, i - 1), self.recursive(K, N - i))
            min_count = min(min_count, count + 1)
        self.dp[K][N] = min_count
        return min_count
