class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        if nums[0] > target or nums[-1] < target:
            return [-1, -1]
        
        length = len(nums)
        left = 0
        right = length - 1
        mid = (left + right) // 2
        
        while left <= right:
            if nums[mid] > target:
                right = mid - 1
                mid = (left + right) // 2
            
            elif nums[mid] < target:
                left = mid + 1
                mid = (left + right) // 2
                
            elif nums[mid] == target:
                left, right = mid, mid
                while left - 1 >= 0 and nums[left - 1] == target:
                    left -= 1
                
                while right + 1 < length and nums[right + 1] == target:
                    right += 1
                    
                return [left, right]
        else:
            return [-1, -1]

