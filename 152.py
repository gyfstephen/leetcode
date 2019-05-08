# coding=utf-8
# https://leetcode-cn.com/problems/maximum-product-subarray/comments/


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = [0] * len(nums), [0] * len(nums)
        a[0] = nums[0]
        b[-1] = nums[-1]
        for i in range(1, len(nums), 1):
            if a[i - 1] != 0:
                a[i] = nums[i] * a[i - 1]
            else:
                a[i] = nums[i]
            if b[len(nums) - i] != 0:
                b[len(nums) - i - 1] = nums[len(nums) - i - 1] * b[len(nums) - i]
            else:
                b[len(nums) - i - 1] = nums[len(nums) - i - 1]
        return max(max(a), max(b))
