class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        if not nums:
            return ans
        
        length = len(nums)
        for i in range(length - k + 1):
            val = max(nums[i: i + k])
            ans.append(val)
        
        return ans

