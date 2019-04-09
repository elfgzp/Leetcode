#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
# https://leetcode-cn.com/problems/count-primes/description/
#
# algorithms
# Easy (25.74%)
# Total Accepted:    14.6K
# Total Submissions: 54.5K
# Testcase Example:  '10'
#
# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#
#
#


class Solution1:
    def countPrimes(self, n: int) -> int:
        count = 0

        for i in range(n):
            if self.isPrime(i):
                count += 1

        return count

    def isPrime(self, n) -> bool:
        if n < 2:
            return False

        if n == 2:
            return True

        i = 2

        while i <= int(n ** 0.5):

            if n % i == 0:
                return False

            i += 1

        return True


class Solution2:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        arr = [0] * n

        for i in range(2, n):

            j = 2
            mul = i * j

            while mul < n:

                arr[mul] = 1
                j += 1
                mul = i * j

        return len(list(filter(lambda x: x == 0, arr[2:])))


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        arr = [1] * n

        for i in range(2, int(n)):
            if arr[i] == 1:
                arr[2*i:n:i] = [0] * len(arr[2*i:n:i])

        return sum(arr[2:])




