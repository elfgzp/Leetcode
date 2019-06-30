class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)
        if length < 2:
            return
        
        i = length - 2
        
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        
        start = i
        if start < 0:
            nums.reverse()
            return
        
        i = start + 1
        while i < length:
            if nums[start] >= nums[i]:
                break
            
            i += 1
        
        end = i - 1
        
        nums[start], nums[end] = nums[end], nums[start]
        tmp = nums[start + 1:]
        tmp.reverse()
        
        nums[start + 1:] = tmp
