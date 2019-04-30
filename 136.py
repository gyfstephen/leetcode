# coding=utf-8
# https://leetcode-cn.com/problems/single-number/


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in nums:
            i = i ^ j
        return i
