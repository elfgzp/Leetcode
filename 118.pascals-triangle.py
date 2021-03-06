#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (59.35%)
# Total Accepted:    19.9K
# Total Submissions: 32.6K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
#
#

class Solution:
    cache = {}
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = []
        for row in range(numRows):
            each = []
            for col in range(row + 1):
                each.append(self._generate(row, col))
            ans.append(each)
        
        return ans
    
    def _generate(self, row: int, col: int) -> int:
        if row < 2:
            return 1
        
        if col == 0:
            return 1
        
        if col == row:
            return 1
        
        if (row, col) not in self.cache.keys():
            self.cache[(row, col)] = self._generate(row - 1, col - 1) + self._generate(row - 1, col)
        
        return self.cache[(row, col)]
        
class Solution1(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if i - 1 < 0:
                    row.append(1)
                    continue

                if j - 1 < 0:
                    row.append(1)
                    continue

                if j > i - 1:
                    row.append(1)
                    continue

                row.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(row)
        return res

