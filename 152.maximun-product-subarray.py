class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        _max, _min, ans = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            _tmp_min = min(_max * num, _min * num, num)
            _tmp_max = max(_max * num, _min * num, num)
            ans = max(ans, _tmp_max)
            
            _min = _tmp_min
            _max = _tmp_max
            
        return ans

