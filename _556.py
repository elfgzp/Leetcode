# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = list(str(n))
        n = len(nums)
        i = n - 1

        if i == 0:
            return -1

        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        self.reverse(nums, i, n - 1)

        for j in range(i, n):
            if nums[j] > nums[i - 1]:
                self.swap(nums, i - 1, j)
                break

        ans = int("".join(nums))

        if ans > 2 ** 32:
            return -1
        else:
            return ans

    def reverse(self, nums, i, j):
        """
        contains i and j.
        """
        for k in range(i, int((i + j) / 2) + 1):
            self.swap(nums, k, i + j - k)

    def swap(self, nums, i, j):
        """
        contains i and j.
        """
        nums[i], nums[j] = nums[j], nums[i]


# 思路： 1、从个位数向左定位到第一个高位小于低位的位置；
#  2、从低位中找出大于高位的最小值所在的位置；
#  3、交换1和2中两个位置的元素；
#  4、高位后元素升序排列。
#  注意：考虑到有可能转换之后的数大于int的最大值，故先将其转化成double类型的数。

class Solution2(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = list(str(n))
        i = len(nums) - 1

        if i == 0:
            return -1

        val = -1
        while i > 0:
            if nums[i - 1] < nums[i]:

                des = nums[i - 1]

                _min = nums[i]
                _min_index = i
                j = i

                while j + 1 < len(nums):
                    if des < nums[j + 1] < _min:
                        _min = nums[j + 1]
                        _min_index = j + 1
                    j += 1

                nums[i - 1], nums[_min_index] = nums[_min_index], nums[i - 1]

                nums = nums[:i] + sorted(nums[i:], key=lambda r: r)
                val = int(''.join(nums))
                break
            i -= 1

        if val > 2 ** 31:
            return -1
        else:
            return val


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement(2147483647
))

    s2 = Solution2()
    print(s2.nextGreaterElement(2147483647
))

# 12443322 13443222
# 13222344


# 230241
# 230412
# 230412

# 12345
# 12354
# 12534
# 12543
# 15234
# 15243
# 15423
# 15432
# 51234
# 51243
# 51423
# 51432
# 54123
# 54132
# 54312
# 54321

b''