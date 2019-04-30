# coding=utf-8
# https://leetcode-cn.com/problems/container-with-most-water/


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_size = (right - left) * min(height[left], height[right])
        while left < right:
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
            size = (right - left) * min(height[left], height[right])
            max_size = max(size, max_size)
        return max_size
