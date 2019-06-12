class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums2, nums1 = nums1, nums2
            
        ans = []
        for num in nums1:
            if num in nums2 and num not in ans:
                ans.append(num)
        
        return ans
            
