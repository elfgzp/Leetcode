#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (41.40%)
# Total Accepted:    7.1K
# Total Submissions: 16.8K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next:
            return head

        cur, pre = head, None
        i = 1

        while i < m:
            pre, cur = cur, cur.next
            i += 1

        t1, t2 = pre, cur
        while i <= n:
            cur.next, pre, cur = pre, cur, cur.next
            i += 1

        if m == 1:
            t2.next = cur
            return pre

        t1.next = pre
        t2.next = cur
        return head


