#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for copy in res[:]:
                tmp = copy[:]
                tmp.append(num)
                res.append(tmp)
        return res
