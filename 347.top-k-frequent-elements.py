#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前K个高频元素
#
# https://leetcode-cn.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (53.32%)
# Total Accepted:    9K
# Total Submissions: 16.6K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
#
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]
#
# 说明：
#
#
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
#
#
#


class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        counter = Counter(nums)

        i = 1
        res = []
        for n, _ in sorted(counter.items(), key=lambda x: x[1], reverse=True):
            res.append(n)
            if i >= k:
                break
            i += 1
        return res

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        return [t[0] for t in c.most_common(k)]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for n in nums:
            m[n] = m.get(n, 0) + 1
        
        tl = [each for each in m.items()]
        
        tl.sort(key=lambda x: -x[1])
        
        return [each[0] for each in tl[:k]]

