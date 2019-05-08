# coding=utf-8
# https://leetcode-cn.com/problems/rotate-array/


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        right = k
        left = len(nums) - k
        k = min(left, right)
        while k > 0:
            k = k - 1
            if right <= left:
                tmp = nums[-1]
                for i in range(len(nums) - 1, 0, -1):
                    nums[i] = nums[i - 1]
                nums[0] = tmp
            else:
                tmp = nums[0]
                for i in range(0, len(nums) - 1, 1):
                    nums[i] = nums[i + 1]
                nums[-1] = tmp
