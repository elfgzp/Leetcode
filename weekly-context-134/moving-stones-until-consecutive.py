class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c], key=lambda x: x)
        b_l, b_r = b - 1, b + 1

        max_moves = 0
        min_moves = 2

        if a == b_l and c == b_r:
            return [0, 0]

        if a != b_l:
            max_moves += b_l - a

        if c != b_r:
            max_moves += c - b_r

        if b_l - a == 1 or c - b_r == 1:
            min_moves = 1
        elif a == b_l or c == b_r:
            min_moves = 1

        return [min_moves, max_moves]
