class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        num, _ = c.most_common()[0]
        return num
        
