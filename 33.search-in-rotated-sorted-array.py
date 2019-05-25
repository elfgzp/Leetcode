class Solution:
    def search(self, nums: List[int], target: int) -> int:
        point = self.find_point(nums)
        index = self.bsearch(nums[:point], target)
        if index != -1:
            return index
        
        index = self.bsearch(nums[point:], target)
        
        if index != -1:
            index += point
        
        return index
    
    def find_point(self, nums) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    def bsearch(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
            
        return -1
            

