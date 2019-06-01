class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        length = len(A)
        left, right = 0, length
        while left <= right:
            mid = (left + right) // 2
            if A[mid] > mid:
                right = mid - 1
            elif A[mid] < mid:
                left = mid + 1
            else:
                return mid
        else:
            return -1

