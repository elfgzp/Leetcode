#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
        len_a = 0
        node = headA
        while node:
            len_a += 1
            node = node.next

        len_b = 0
        node = headB
        while node:
            len_b += 1
            node = node.next

        if len_a > len_b:
            skip = len_a - len_b
            node1 = headA
            node2 = headB
            length = len_b
        else:
            skip = len_b - len_a
            node1 = headB
            node2 = headA
            length = len_a

        for _ in range(skip):
            node1 = node1.next

        for _ in range(length):
            if node1 == node2:
                return node1
            node1 = node1.next
            node2 = node2.next
        else:
            return None



