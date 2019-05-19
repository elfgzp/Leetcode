#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (55.90%)
# Total Accepted:    19.3K
# Total Submissions: 34.2K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#
#
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
#
# 说明:
#
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
#
#


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #self._qsort(nums, 0, len(nums) - 1)
        nums = self._msort(nums)
        return nums[k - 1]

    def _qsort(self, nums, start, end):
        if start >= end:
            return

        pivot = start
        left = pivot
        right = end

        while left < right:
            while left < right and nums[right] < nums[pivot]:
                right -= 1

            while left < right and nums[left] >= nums[pivot]:
                left += 1

            nums[left], nums[right] = nums[right], nums[left]

        nums[left], nums[pivot] = nums[pivot], nums[left]

        self._qsort(nums, start, left - 1)
        self._qsort(nums, left + 1, end)

    def _msort(self, nums):
        """
        归并排序
        """
        length = len(nums)
        if length < 2:
            return nums

        mid = length // 2

        left = self._msort(nums[:mid])
        right = self._msort(nums[mid:])

        tmp = []
        while left and right:
            if left[0] > right[0]:
                tmp.append(left.pop(0))
            else:
                tmp.append(right.pop(0))

        if left:
            tmp += left
        else:
            tmp += right

        return tmp


