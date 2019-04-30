# coding=utf-8
# https://leetcode-cn.com/problems/reverse-linked-list/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p, q = head, head.next
        head.next = None
        while q:
            r = q.next
            q.next = p
            p, q = q, r
        return p
