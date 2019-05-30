class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            val = 1 / self._myPow(x, -n)
        else:
            val = self._myPow(x, n)
        return val

    def _myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1
        else:
            half = n // 2
            remainder = n - 2 * half
            val = self._myPow(x, half)
            val *= val

            if remainder > 0:
                val *= x

            return val


