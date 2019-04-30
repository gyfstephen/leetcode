# coding=utf-8
# https://leetcode-cn.com/problems/rotate-list/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # 计算第X个元素做新头
        tmp = head
        linklist_len = 0
        while tmp:
            tmp = tmp.next
            linklist_len += 1
        step = linklist_len - k % linklist_len
        # 如果移动步数为0或者整个链表长度 直接返回
        if step == 0 or step == linklist_len:
            return head
        # 根据步数向后移动指针，新尾指向空，生成新头
        tmp = head
        old_head = head
        while step > 0:
            if step == 1:
                new_tail = tmp
                tmp = tmp.next
                new_tail.next = None
            else:
                tmp = tmp.next
            step -= 1
        new_head = tmp
        # 向后移动指针，找到老尾指向老头
        while tmp:
            if tmp.next is None:
                tmp.next = old_head
                break
            else:
                tmp = tmp.next
        # 返回新头
        return new_head
