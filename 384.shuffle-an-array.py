#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#
# https://leetcode-cn.com/problems/shuffle-an-array/description/
#
# algorithms
# Medium (43.25%)
# Total Accepted:    5.4K
# Total Submissions: 12.3K
# Testcase Example:  '["Solution","shuffle","reset","shuffle"]\n[[[1,2,3]],[],[],[]]'
#
# 打乱一个没有重复元素的数组。
# 
# 示例:
# 
# 
# // 以数字集合 1, 2 和 3 初始化数组。
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
# 
# // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
# solution.shuffle();
# 
# // 重设数组到它的初始状态[1,2,3]。
# solution.reset();
# 
# // 随机返回数组[1,2,3]打乱后的结果。
# solution.shuffle();
# 
# 

class Solution:
    
    def __init__(self, nums: List[int]):
        self._origin = nums[:]
        self._nums = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self._nums[:] = self._origin[:]
        return self._nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        
        length = len(self._nums)
        for i in range(length):
            randi = random.randint(0, length - 1)
            self._nums[i], self._nums[randi] = self._nums[randi], self._nums[i]
        
        return self._nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

