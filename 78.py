# coding=utf-8
# https://leetcode-cn.com/problems/subsets


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            tmp = nums[i]
            if ans:
                for j in range(0, len(ans), 1):
                    ans.append(ans[j] + [tmp])
                ans.append([tmp])
            else:
                ans = [[tmp]]
        ans.append([])
        return ans
