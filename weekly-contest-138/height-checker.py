class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_heights = sorted(heights, key=lambda x: x)
        length = len(new_heights)
        
        ans = 0
        for i in range(length):
            if new_heights[i] != heights[i]:
                ans += 1
        
        return ans
        

