class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        
        while left <= right:

            day_weight = 0
            day = 1
            mid = (left + right) // 2

            for w in weights:
                if day_weight + w <= mid:
                    day_weight += w
                else:
                    day_weight = w
                    day += 1
            
            if day > D:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
