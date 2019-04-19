#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.62%)
# Total Accepted:    116.1K
# Total Submissions: 343.7K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nums1 = []
        while l1:
            nums1.append(l1.val)
            l1 = l1.next

        nums2 = []
        while l2:
            nums2.append(l2.val)
            l2 = l2.next

        if len(nums1) >= len(nums2):
            lg = nums1
            lt = nums2
        else:
            lg = nums2
            lt = nums1

        i = 0
        carry = 0
        res = []
        while i < len(lt):
            _sum = lg[i] + lt[i] + carry
            if _sum >= 10:
                carry = 1
            else:
                carry = 0
            res.append(_sum % 10)
            i += 1

        while i < len(lg):
            _sum = lg[i] + carry
            if _sum >= 10:
                carry = 1
            else:
                carry = 0
            res.append(_sum % 10)
            i += 1

        if carry:
            res.append(carry)

        if not res:
            return None

        root = ListNode(res[0])
        node = root
        for i in range(1, len(res)):
            node.next = ListNode(res[i])
            node = node.next

        return root


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        _sum = (l1.val if l1 else 0) + (l2.val if l2 else 0)
        carry = _sum // 10

        root = ListNode(_sum % 10)

        l1, l2 = l1.next, l2.next
        node = root
        while l1 or l2 or carry:
            _sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = _sum // 10
            node.next = ListNode(_sum % 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            node = node.next

        return root



