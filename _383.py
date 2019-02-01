# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for s in ransomNote:
            index_s = magazine.find(s)
            if index_s < 0:
                return False

            magazine = magazine[:index_s] + magazine[index_s + 1:]

        return True
