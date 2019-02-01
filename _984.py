# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        a = ['a'] * A
        b = ['b'] * B
        res = []
        while a or b:

            if A > B:
                if a:
                    res.append(a.pop(0))
                    A -= 1
                    if a:
                        res.append(a.pop(0))
                        A -= 1
                if b:
                    res.append(b.pop(0))
                    B -= 1
            elif A < B:
                if b:
                    res.append(b.pop(0))
                    B -= 1
                    if b:
                        res.append(b.pop(0))
                        B -= 1
                if a:
                    res.append(a.pop(0))
                    A -= 1

            if abs(A - B) <= 1:
                if res:
                    if res[-1] == 'a':
                        if b:
                            res.append(b.pop(0))
                            B -= 1
                        if a:
                            res.append(a.pop(0))
                            A -= 1
                    else:
                        if a:
                            res.append(a.pop(0))
                            A -= 1
                        if b:
                            res.append(b.pop(0))
                            B -= 1
                else:
                    if a:
                        res.append(a.pop(0))
                        A -= 1
                    if b:
                        res.append(b.pop(0))
                        B -= 1

        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.strWithout3a3b(2, 3))
