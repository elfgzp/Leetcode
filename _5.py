# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution(object):
    _cache = set()

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        i = 0
        lpd = ''
        while i < len(s):
            j = i
            while j < len(s):
                sub = s[i:j + 1]
                if len(sub) == 1 and len(sub) >= len(lpd):
                    lpd = sub

                else:
                    left, right = 0, len(sub) - 1
                    while left < len(sub) / 2 <= right:
                        if sub[left] != sub[right]:
                            break

                        if sub[left + 1:right] in self._cache:
                            if len(sub) > len(lpd):
                                lpd = sub
                            self._cache.add(sub)
                            break
                        else:
                            left += 1
                            right -= 1
                    else:
                        self._cache.add(sub)

                        if len(sub) >= len(lpd):
                            lpd = sub

                j += 1

            i += 1

        return lpd


class Solution2(object):
    """
    最优解
    """

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_length = len(s)
        max_length = 0
        start = 0
        for i in range(str_length):
            if i - max_length >= 1 and s[i - max_length - 1: i + 1] == s[i - max_length - 1: i + 1][::-1]:
                start = i - max_length - 1
                max_length += 2
                continue
            if i - max_length >= 0 and s[i - max_length: i + 1] == s[i - max_length: i + 1][::-1]:
                start = i - max_length
                max_length += 1
        return s[start: start + max_length]


class Solution3(object):
    def longestPalindrome(self, s):
        k = len(s)
        matrix = [[0 for i in range(k)] for i in range(k)]
        logestSubStr = ""
        logestLen = 0

        for j in range(0, k):
            for i in range(0, j + 1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        matrix[i][j] = 1
                        if logestLen < j - i + 1:
                            logestSubStr = s[i:j + 1]  # 取当前的最长回文子串
                            logestLen = j - i + 1  # 当前最长回文子串的长度
                else:
                    if s[i] == s[j] and matrix[i + 1][j - 1]:
                        matrix[i][j] = 1
                        if logestLen < j - i + 1:
                            logestSubStr = s[i:j + 1]
                            logestLen = j - i + 1

        return logestSubStr


class Solution4(object):
    """Learning"""

    def longestPalindrome(self, s):
        len_s = len(s)
        m = [[False for _ in range(len_s)] for _ in range(len_s)]

        max_len = 0
        max_sub = ''

        for j in range(len_s):
            for i in range(j + 1):
                if j - i <= 1 and s[j] == s[i]:
                    m[i][j] = True
                    if len(s[i: j + 1]) > max_len:
                        max_len = len(s[i: j + 1])
                        max_sub = s[i: j + 1]

                if j - i > 1 and s[j] == s[i] and m[i + 1][j - 1]:
                    m[i][j] = True
                    if len(s[i: j + 1]) > max_len:
                        max_len = len(s[i: j + 1])
                        max_sub = s[i: j + 1]

        return max_sub


if __name__ == '__main__':
    s = Solution4()
    print(s.longestPalindrome("babad"))
    # print(s.longestPalindrome('cbbd'))
    # print(s.longestPalindrome(
    #     "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))
    # print(s.longestPalindrome(
    #     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
