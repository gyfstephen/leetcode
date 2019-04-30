# coding=utf-8
# https://leetcode-cn.com/problems/merge-k-sorted-lists/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def merge2List(self, l1, l2):
        head = ListNode(0)
        temp = head
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.merge2List(lists[0], lists[1])
        else:
            temp = self.merge2List(lists[0], lists[1])
            for i in range(2, len(lists), 1):
                temp = self.merge2List(temp, lists[i])
        return temp
