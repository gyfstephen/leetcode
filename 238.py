# coding=utf8
# https://leetcode-cn.com/problems/product-of-array-except-self/comments/


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_n = len(nums)
        ans = [1] * len_n
        left, right = 1, 1
        for idx, i in enumerate(nums):
            ans[idx] = ans[idx] * left
            left = left * nums[idx]
            ans[len_n - idx - 1] = ans[len_n - idx - 1] * right
            right = right * nums[len_n - idx - 1]
        return ans
