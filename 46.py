# coding=utf-8
# https://leetcode-cn.com/problems/permutations/


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        if len(nums) == 1:
            return [nums]
        ans = list()
        for idx, i in enumerate(nums):
            tmp = nums[0: idx] + nums[idx + 1:]
            for j in self.permute(tmp):
                ans.append([i] + j)
        return ans
