class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a = ((points[0][0] - points[1][0])**2 + (points[0][1] - points[1][1])**2) ** (1 / 2)
        b = ((points[0][0] - points[2][0])**2 + (points[0][1] - points[2][1])**2) ** (1 / 2)
        c = ((points[1][0] - points[2][0])**2 + (points[1][1] - points[2][1])**2) ** (1 / 2)

        for line in (a, b, c):
            if line <= 0:
                return False

        if a + b <= c or a + c <= b or b + c <= a:
            return False

        return True
