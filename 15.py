# coding=utf-8
# https://leetcode-cn.com/problems/3sum/


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ans = list()
        for i in range(0, len(nums) - 2, 1):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    j += 1
                    k -= 1
                    ans.append((nums[i], nums[j], nums[k]))
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
        return list(set(ans))
