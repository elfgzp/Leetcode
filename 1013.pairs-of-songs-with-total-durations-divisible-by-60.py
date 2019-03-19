class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        一个数的余数为X,它只需要另一个数的余数为60-X,这两个数之和就能被60整除

        当 X % 60 = 30 和 X % 60 = 0 做特殊处理
        例如                    time = [60, 60, 60, 60, 60, 60]
        他们分别对应的另一半数量为         [5,  4,  3,  2,  1,  0 ] （注意题意 i < j）
        则 sum([5,  4,  3,  2,  1,  0 ]) = (1 + 5) / 2 * 5      （等差数列求和）
        """
        from collections import Counter
        
        c = Counter()
        for t in time:
            c[t % 60] += 1
        
        _30 = (1 + c[30] - 1) / 2 * (c[30] - 1) # 或 sum(range(c[30]))
        _0 = (1 + c[0] - 1) / 2 * (c[0] - 1)  # 或 sum(range(c[0]))
        
        return sum(c[x] * c[60 - x] for x in c.keys() if 0 < x < 30) + int(_30) + int(_0)
