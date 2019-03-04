class Solution1:
    def isValid(self, S: str) -> bool:
        S2 = ""
        while S != S2:
            S, S2 = S.replace("abc", ""), S
        return S == ""


class Solution:
    def isValid(self, S: str) -> bool:
        inn = []

        for s in S:
            if s == 'c':
                if len(inn) >= 2 and inn[-1:-3:-1] == ['b', 'a']:
                    inn.pop()
                    inn.pop()
                else:
                    return False

            else:
                inn.append(s)
        return len(inn) == 0
