# coding=utf-8
# https://leetcode-cn.com/problems/maximum-subarray/


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp[0] = nums[0]
        for i in range(1, len(nums), 1):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)
