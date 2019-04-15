#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode-cn.com/problems/group-anagrams/description/
#
# algorithms
# Medium (53.98%)
# Total Accepted:    14K
# Total Submissions: 25.5K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
#
# 说明：
#
#
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
#
#
# class Solution1:


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    m = {}
    for s in strs:
        s_sorted = ''.join(sorted(s))
        res = m.get(s_sorted)
        if res is None:
            m[s_sorted] = [s]
        else:
            res.append(s)
    return list(m.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        利用质数 map 来解题
        """
        pn = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

        i = 97
        pnm = {chr(i + j): pn[j] for j in range(26)}
        m = {}
        for s in strs:
            val = None
            for c in s:
                if not val:
                    val = pnm[c]
                else:
                    val *= pnm[c]

            res = m.get(val)
            if res is None:
                m[val] = [s]
            else:
                res.append(s)
        return list(m.values())
