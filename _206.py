# -*- coding: utf-8 -*-
__author__ = 'gzp'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p, rev = head, None

        while p:
            rev, rev.next, p = p, rev, p.next

        return rev






