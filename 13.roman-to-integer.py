#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#


class Solution:
    hash_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        sum_s = 0
        len_s = len(s)
        for i in range(len_s):
            cur = self.hash_map[s[i]]
            if i < len_s - 1 and cur < self.hash_map[s[i + 1]]:
                sum_s -= cur
            else:
                sum_s += cur
        return sum_s



