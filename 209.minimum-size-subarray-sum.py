class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        ans = float('inf')
        _sum = 0
        left = 0
        
        for right in range(len(nums)):
            _sum += nums[right]
            while _sum >= s:
                _sum -= nums[left]
                ans = min(ans, right - left + 1)
                left += 1
            
        return ans if ans != float('inf') else 0

