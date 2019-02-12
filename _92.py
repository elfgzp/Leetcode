# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m >= n or m < 0 or n < 0:
            return head

        cur, pre = head, None
        i = 1

        while i < m and cur:
            pre, cur = cur, cur.next
            i += 1

        t1, t2 = pre, cur
        while i <= n and cur:
            cur.next, pre, cur = pre, cur, cur.next
            i += 1

        if m == 1:
            t2.next = cur
            return pre

        t1.next = pre
        t2.next = cur
        return head
