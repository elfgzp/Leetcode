from typing import List


class Solution1:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = []
        for r in range(R):
            for c in range(C):
                res.append([[r, c], abs(c - c0) + abs(r - r0)])

        res.sort(key=lambda x: x[1])
        res = [x[0] for x in res]
        return res


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        cells = [(r, c) for c in range(C) for r in range(R)]
        cells.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return cells
