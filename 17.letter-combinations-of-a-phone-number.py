#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#


class Solution:
    h = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        length = len(digits)

        stack = []
        results = []

        stack = [[0, 0]]
        res = ''
        while stack:
            i, j = stack[-1]

            strs = self.h[digits[i]]

            if j < len(strs):
                if i < length - 1:
                    res += strs[j]
                    i += 1
                    stack.append([i, 0])
                else:
                    res += strs[j]
                    results.append(res)
                    res = res[:-1]
                    stack[-1][1] = stack[-1][1] + 1
            else:
                stack.pop(-1)
                if stack:
                    stack[-1][1] = stack[-1][1] + 1
                    res = res[:-1]

        return results



