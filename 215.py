# coding=utf-8
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k]
