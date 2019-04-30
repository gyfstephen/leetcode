# coding=utf-8
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/comments/


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        last = nums[0]
        offset = 0
        for i in range(1, len(nums), 1):
            if nums[i] != last:
                last = nums[i]
                nums[i - offset] = last
            else:
                offset += 1
        return len(nums) - offset
