# coding=utf-8
# https://leetcode-cn.com/problems/3sum-closest/


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        sum = nums[0] + nums[1] + nums[2]
        diff = abs(nums[0] + nums[1] + nums[2] - target)
        for i in range(0, len(nums), 1):
            first = nums[i]
            i = i + 1
            j = len(nums) - 1
            while i < j:
                if abs(nums[i] + nums[j] + first - target) < diff:
                    sum = nums[i] + nums[j] + first
                    diff = abs(sum - target)
                if nums[i] + nums[j] + first > target:
                    j -= 1
                elif nums[i] + nums[j] + first < target:
                    i += 1
                if diff == 0:
                    return target
        return sum
