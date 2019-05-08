# coding=utf-8
# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = set(nums1) & set(nums2)
        ans = list()
        for i in inter:
            ans += [i] * min(nums1.count(i), nums2.count(i))
        return ans
