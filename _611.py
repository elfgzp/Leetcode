# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        res = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                k = j + 1
                while k < len(nums):
                    a, b, c, = sorted([nums[i], nums[j], nums[k]], key=lambda r: r)
                    if a + b > c and c - b < a:
                        res += 1
                    k += 1
                j += 1
            i += 1

        return res


class Solution2:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        res = 0
        for i in range(2, len(nums)):
            left, right = 0, i - 1
            while right > left:
                if nums[right] + nums[left] > nums[i]:
                    res += (right - left)
                    right -= 1
                else:
                    left += 1
        return res


#
# [81, 38, 2, 80, 26, 52, 59, 7, 10, 23, 88, 79, 60, 53, 67, 49, 31, 93, 67, 54, 57, 1, 70, 63, 71, 99, 93, 43, 94, 33,
#  38, 53, 85, 83, 99, 44, 11, 20, 68, 26, 62, 40, 3, 97, 19, 30, 65, 23, 19, 16, 58, 9, 1, 51, 43, 64, 23, 22, 51, 72,
#  18, 20, 79, 85, 25, 93, 15, 11, 63, 94, 61, 29, 82, 2, 6, 53, 23, 58, 80, 60, 73, 81, 65, 79, 22, 64, 39, 58, 83, 42,
#  40, 93, 16, 34, 53, 19, 73, 31, 35, 92]


if __name__ == '__main__':
    s = Solution()
    print(s.triangleNumber([2, 2, 3, 4]))

    s = Solution2()
    print(s.triangleNumber([2, 2, 3, 4]))
