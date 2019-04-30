# coding=utf-8
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        len_1 = len(nums1)
        len_2 = len(nums2)
        if not len_1:
            if len_2 % 2 == 1:
                return nums2[len_2 / 2]
            else:
                return (nums2[len_2 / 2] + nums2[len_2 / 2 - 1]) / 2.0
        if not len_2:
            if len_1 % 2 == 1:
                return nums1[len_1 / 2]
            else:
                return (nums1[len_1 / 2] + nums1[len_1 / 2 - 1]) / 2.0
        i, j, tmp = 0, 0, list()
        while i < len_1 and j < len_2:
            if nums1[i] < nums2[j]:
                tmp.append(nums1[i])
                i += 1
            else:
                tmp.append(nums2[j])
                j += 1
        if i == len_1:
            tmp += nums2[j:]
        if j == len_2:
            tmp += nums1[i:]
        if (len_1 + len_2) % 2 == 1:
            return tmp[(len_1 + len_2) / 2]
        else:
            return (tmp[(len_1 + len_2) / 2] + tmp[(len_1 + len_2) / 2 - 1]) / 2.0
