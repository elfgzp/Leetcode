class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
         Do not return anything, modify nums in-place instead.
        """
        self._qsort(nums, 0, len(nums) - 1)

    def _qsort(self, nums, start, end):
        if start >= end:
            return
        
        pivot = start
        left = start
        right = end
        while left < right:
            while left < right and nums[right] > nums[pivot]:
                right -= 1

            while left < right and nums[left] <= nums[pivot]:
                left += 1

            nums[left], nums[right] = nums[right], nums[left]

        nums[left], nums[pivot] = nums[pivot], nums[left]

        self._qsort(nums, start, left - 1)
        self._qsort(nums, left + 1, end)

            
        
