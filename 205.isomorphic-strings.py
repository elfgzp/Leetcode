#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#


class Solution1(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s = len(s)

        map_s = {}
        map_t = {}
        for i in range(len_s):
            s_char = s[i]
            t_char = t[i]

            if s_char in map_s.keys() and map_s[s_char] != t_char:
                return False
            elif t_char in map_t.keys() and map_t[t_char] != s_char:
                return False
            else:
                map_s[s_char] = t_char
                map_t[t_char] = s_char

        else:
            return True


class Solution2(object):
    def isIsomorphic(self, s, t):
        """
        这个比第一个快？为什么？
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s = len(s)

        map_s = {}
        map_t = {}
        for i in range(len_s):
            s_char = s[i]
            t_char = t[i]

            if s_char in map_s.keys():
                if map_s[s_char] != t_char:
                    return False
            elif t_char in map_t.keys():
                if map_t[t_char] != s_char:
                    return False

            else:
                map_s[s_char] = t_char
                map_t[t_char] = s_char

        else:
            return True
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        temp = {}
        for i in range(len(s)):
            if s[i] not in temp:
                temp[s[i]] = t[i]
                if len(temp.values()) != len(set(temp.values())):
                    return False
            if temp[s[i]] != t[i]:
                return False
        return True
