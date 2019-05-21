class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(float('-inf'))
        length = len(nums)
        i = 1
        while i + 1 < length:
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                return i
            
            i += 1
        else:
            return 0

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        
        return left


