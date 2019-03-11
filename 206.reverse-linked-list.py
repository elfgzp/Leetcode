#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (58.01%)
# Total Accepted:    38.9K
# Total Submissions: 66.5K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        node, last = head, None

        while node:
            tmp_last = last
            last = node

            tmp_node_next = node.next
            last.next = tmp_last

            node = tmp_node_next

        return last


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        last = self._reverseList(head, None)
        return last

    def _reverseList(self, node, last):
        if not node:
            return last

        next_node = node.next
        node.next = last
        last = node

        return self._reverseList(next_node, last)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, last = head, None

        while node:
            last, last.next, node = node, last, node.next

        return last


