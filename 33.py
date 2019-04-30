# coding=utf-8
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/comments/


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        return self.search_func(nums, left, right, target)

    def search_func(self, nums, left, right, target):
        if left > right:
            return -1
        mid = (left + right) / 2
        if nums[mid] == target:
            return mid
        if nums[mid] < nums[right]:
            if nums[mid] < target <= nums[right]:
                return self.search_func(nums, mid + 1, right, target)
            else:
                return self.search_func(nums, left, mid - 1, target)
        else:
            if nums[left] <= target < nums[mid]:
                return self.search_func(nums, left, mid - 1, target)
            else:
                return self.search_func(nums, mid + 1, right, target)
