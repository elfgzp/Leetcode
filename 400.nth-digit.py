#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第N个数字
#


class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n

        i = 1
        length = 0
        cnt = 9

        while length + cnt * i < n:
            length += cnt * i
            cnt *= 10
            i += 1

        num = pow(10, i-1) - 1 + (n - length + 1) // i
        index = (n - length - 1) % i

        return int(str(num)[index])

