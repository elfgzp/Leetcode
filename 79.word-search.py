#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (35.56%)
# Total Accepted:    6.2K
# Total Submissions: 17.4K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 示例:
#
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
#
#


class Solution:
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    board = []
    h = 0
    w = 0

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True

        if not board:
            return False

        self.h = len(board)
        self.w = len(board[0])
        self.board = board

        for i in range(self.h):
            for j in range(self.w):
                if self._exist(word, 0, i, j):
                    return True

        return False

    def _exist(self, word, word_index, x, y):

        if word_index + 1 == len(word):
            return self.board[x][y] == word[word_index]

        if self.board[x][y] == word[word_index]:
            for d_x, d_y in self.direction:
                _x = x + d_x
                _y = y + d_y

                tmp = self.board[x][y]
                self.board[x][y] = '#'

                if self._inrange(_x, _y) and self._exist(word, word_index + 1, _x, _y):
                    return True

                self.board[x][y] = tmp

        return False

    def _inrange(self, x, y):
        return 0 <= x < self.h and 0 <= y < self.w
