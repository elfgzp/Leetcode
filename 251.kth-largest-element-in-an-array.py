class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # self._qsort(nums, 0, len(nums) - 1)
        nums = self._msort(nums)
        return nums[k - 1]
        
    def _qsort(self, nums, start, end):
        if start >= end:
            return
        
        pivot = nums[start]
        left = start
        right = end
        
        while left < right:   
            while left < right and nums[right] < pivot:
                right -= 1
                
            nums[left], nums[right] = nums[right], nums[left]

            while left < right and nums[left] >= pivot:
                left += 1
                
            nums[left], nums[right] = nums[right], nums[left]
        
            
        nums[left], pivot = pivot, nums[left]
        
        self._qsort(nums, start, left - 1)
        self._qsort(nums, left + 1, end)
        
            
    def _msort(self, nums):
        """
        归并排序
        """
        length = len(nums)
        if length < 2:
            return nums
        
        mid = length // 2
        
        left = self._msort(nums[:mid])
        right = self._msort(nums[mid:])
        
        tmp = []
        while left and right:
            if left[0] > right[0]:
                tmp.append(left.pop(0))
            else:
                tmp.append(right.pop(0))
        
        if left:
            tmp += left
        else:
            tmp += right
        
        return tmp
            
