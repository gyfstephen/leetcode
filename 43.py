# coding=utf-8
# https://leetcode-cn.com/problems/multiply-strings/


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'

        nums1_list = [int(x) for x in num1]
        nums2_list = [int(x) for x in num2]

        len_nums1 = len(nums1_list)
        len_nums2 = len(nums2_list)

        result = [0] * (len_nums1 + len_nums2 + 1)
        len_result = len(result)

        for i in range(len_nums1 - 1, -1, -1):
            for j in range(len_nums2 - 1, -1, -1):
                idx = len_nums2 - j + len_nums1 - i - 1
                result[-idx] += nums1_list[i] * nums2_list[j]

        tmp = 0
        flag = len_result - 1
        for i in range(len_result - 1, -1, -1):
            result[i] = result[i] + tmp
            if result[i] != 0:
                flag = i
            tmp = result[i]
            result[i] = result[i] % 10
            tmp = tmp / 10
        result = result[flag:]
        return ''.join(str(x) for x in result)
