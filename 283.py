# coding=utf-8
# https://leetcode-cn.com/problems/move-zeroes/


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        count = 0
        for i in range(0, len(nums), 1):
            if nums[i] == 0:
                count += 1
            else:
                nums[i - count] = nums[i]
        if count:
            nums[-count:] = [0] * count
