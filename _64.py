# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        width = len(grid[0])

        for w in range(1, width):
            grid[0][w] = grid[0][w - 1] + grid[0][w]

        for h in range(1, height):
            grid[h][0] = grid[h - 1][0] + grid[h][0]

        for h in range(1, height):
            for w in range(1, width):
                grid[h][w] = min(grid[h][w] + grid[h - 1][w], grid[h][w] + grid[h][w - 1])

        return grid[-1][-1]
