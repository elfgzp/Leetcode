#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (20.04%)
# Total Accepted:    46.7K
# Total Submissions: 214.6K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums or len(nums) < 3:
            return res

        ln = len(nums)
        nums = sorted(nums, key=lambda x: x)
        for i in range(ln - 2):
            # 只循环负数，因为必有一个负数
            if nums[i] > 0:
                break

            # 去重
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left = i + 1
            right = ln - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # 去重
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # 去重
                    while left < right and nums[right] == nums[left - 1]:
                        right += 1

                    right -= 1
                    left += 1

                elif s > 0:
                    right -= 1
                else:
                    left += 1

        return res


