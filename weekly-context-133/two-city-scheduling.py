from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: -(abs(x[0] - x[1])))
        
        half = len(costs) // 2
        count_a = 0
        count_b = 0
        res = 0
        
        for a, b in costs:
            if (a < b and count_a < half) or count_b == half:
                res += a
                count_a += 1
            else:
                res += b
                count_b += 1
                
        
        return res