#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        self.gen(n, n, '', results)
        return results

    def gen(self, left, right, strs, results):
        if left == right == 0:
            results.append(strs)
            return

        if left > 0:
            self.gen(left - 1, right, strs + '(', results)

        if right > left:
            self.gen(left, right - 1, strs + ')', results)

