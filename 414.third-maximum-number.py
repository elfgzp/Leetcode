class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums:
            return float('-inf')
        
        nums = list(set(nums))
        nums.sort(reverse=True)
        
        if len(nums) < 3:
            return nums[0]
        
        return nums[2]
