class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        seats_num = len(seats)
        if seats_num <= 1:
            return 1
        
        ans, start, end = 1, 0, 0
        for i, num in enumerate(seats):
            if num == 1 :
                start, end = end, i
                ans = max(ans, (end - start) // 2)
        
        if seats[0] == 0:
            count, i = 0, 0
            while seats[i] == 0:
                i += 1
                count += 1
            
            ans = max(ans, count)
        
        if seats[-1] == 0:
            count, i = 0, -1
            while seats[i] == 0:
                i -= 1
                count += 1
            ans = max(ans, count)
        
        return ans
