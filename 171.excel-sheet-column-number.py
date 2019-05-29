class Solution:
    m = {
        chr(64 + i): i
        for i in range(1, 27)
    }

    def titleToNumber(self, s: str) -> int:
        length = len(s)
        ans = 0
        for i in range(length):
            c = s[-(i + 1)]
            ans += self.m[c] * 26**i

        return ans

