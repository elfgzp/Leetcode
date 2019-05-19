class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) >= 2:
            stones.sort(key=lambda x: -x)
            y = stones.pop(0)
            x = stones.pop(0)

            z = y - x
            if z > 0:
                stones.append(z)

        if stones:
            return stones[0]

        return 0
