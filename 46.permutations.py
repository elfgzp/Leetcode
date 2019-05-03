#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (65.30%)
# Total Accepted:    13.9K
# Total Submissions: 21.3K
# Testcase Example:  '[1,2,3]'
#
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
#


class Solution:
    """
    2019/05/03
    """
    nums = None
    results = None

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.results = []
        self.gen([])
        return self.results

    def gen(self, com, count=1):
        if count > len(self.nums):
            self.results.append(com)
            return

        for n in self.nums:
            if n in com:
                continue

            if count > 1:
                if count == len(com):
                    com.pop(-1)

                com.append(n)
            else:
                com = [n]

            self.gen(com[::], count + 1)


class Solution1:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        return [list(t) for t in permutations(nums, len(nums))]

