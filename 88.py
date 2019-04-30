# coding=utf-8
# https://leetcode-cn.com/problems/merge-sorted-array/


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        idx = -1
        while m >= 1 and n >= 1:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[idx] = nums1[m - 1]
                m -= 1
            else:
                nums1[idx] = nums2[n - 1]
                n -= 1
            idx -= 1
        if n:
            nums1[0: n] = nums2[0: n]
