class Solution:
    def searchMatrix(self, matrix, target):
        """
                :type matrix: List[List[int]]
                :type target: int
                :rtype: bool
        """
        if not matrix:
            return False

        rows = len(matrix)
        cols = len(matrix[0]) - 1
        row = 0

        while row < rows and cols >= 0:
            if matrix[row][cols] == target:
                return True

            elif matrix[row][cols] < target:
                row += 1
            
            else:
                cols -= 1
        return False


