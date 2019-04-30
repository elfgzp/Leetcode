#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿的个数
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (40.57%)
# Total Accepted:    7.8K
# Total Submissions: 19.3K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给定一个由 '1'（陆地）和
# '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
#
# 示例 1:
#
# 输入:
# 11110
# 11010
# 11000
# 00000
#
# 输出: 1
#
#
# 示例 2:
#
# 输入:
# 11000
# 11000
# 00100
# 00011
#
# 输出: 3
#
#
#


class Solution:
    """
    2019/04/30
    """
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        w = len(grid[0])
        h = len(grid)

        count = 0
        for r in range(h):
            for c in range(w):
                if grid[r][c] == '1':
                    stack = [(r, c, 0)]
                    while stack:
                        r0, c0, d = stack.pop(-1)
                        grid[r0][c0] = 'x'
                        while d < 4:
                            rd, cd = self.d[d]
                            r1, c1 = r0 + rd, c0 + cd

                            d += 1
                            if 0 <= r1 < h and 0 <= c1 < w and grid[r1][c1] == '1':
                                stack.append((r0, c0, d))
                                stack.append((r1, c1, 0))
                                break

                    count += 1
        return count


class Solution1:
    direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    grid = []
    h = 0
    w = 0

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        self.h = len(grid)
        self.w = len(grid[0])
        self.grid = grid

        res = 0
        for i in range(self.h):
            for j in range(self.w):
                if self.grid[i][j] == '1':
                    res += 1
                    self._numIslands(i, j)

        return res

    def _numIslands(self, x, y):
        self.grid[x][y] = '#'

        for d_x, d_y in self.direct:
            _x = x + d_x
            _y = y + d_y
            if self._in_range(_x, _y) and self.grid[_x][_y] == '1':
                self._numIslands(_x, _y)

    def _in_range(self, x, y):
        return 0 <= x < self.h and 0 <= y < self.w

