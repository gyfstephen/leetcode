# coding=utf-8
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tmpA, tmpB = headA, headB
        len_a, len_b = 0, 0
        while tmpA:
            tmpA = tmpA.next
            len_a += 1
        while tmpB:
            tmpB = tmpB.next
            len_b += 1
        if len_a >= len_b:
            for i in range(0, len_a - len_b, 1):
                headA = headA.next
        else:
            for i in range(0, len_b - len_a, 1):
                headB = headB.next
        while headA:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
