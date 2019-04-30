# coding=utf-8
# https://leetcode-cn.com/problems/sort-list/comments/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        return self.minute(head)

    def minute(self, head):
        slow, quick, temp = head, head, head
        if not head.next:
            return head
        while quick and quick.next:
            temp = slow
            slow = slow.next
            quick = quick.next.next
        temp.next = None
        i = self.minute(head)
        j = self.minute(slow)
        return self.combined(i, j)

    def combined(self, i, j):
        head = ListNode(0)
        temp = head
        while i and j:
            if i.val <= j.val:
                temp.next = i
                i = i.next
            else:
                temp.next = j
                j = j.next
            temp = temp.next
        if i:
            temp.next = i
        if j:
            temp.next = j
        return head.next
