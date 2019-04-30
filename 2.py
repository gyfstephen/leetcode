# coding=utf-8
# https://leetcode-cn.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        curr = head
        carry = 0
        while l1 or l2:
            if l1 and l2:
                num = l1.val + l2.val + carry
                carry = num / 10
                num = num % 10
                curr.next = ListNode(num)
                curr = curr.next
                l1, l2 = l1.next, l2.next
            elif l1:
                num = l1.val + carry
                carry = num / 10
                num = num % 10
                curr.next = ListNode(num)
                curr = curr.next
                l1 = l1.next
            elif l2:
                num = l2.val + carry
                carry = num / 10
                num = num % 10
                curr.next = ListNode(num)
                curr = curr.next
                l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
            curr = curr.next
        return head.next
