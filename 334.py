# coding=utf-8
# https://leetcode-cn.com/problems/increasing-triplet-subsequence/comments/

import sys


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = sys.maxint
        b = sys.maxint
        for i in nums:
            if i < a:
                a = i
            elif i < b:
                b = i
            else:
                return True
        return False
