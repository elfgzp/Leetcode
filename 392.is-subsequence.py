class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)

        for c in t:
            if not s:
                return True
            elif s[0] == c:
                s.pop(0)

        return not s
