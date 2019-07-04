class Solution:
    cache = {}
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [self._generate(rowIndex, col) for col in range(rowIndex + 1)]
        return ans
            
        
    def _generate(self, row: int, col: int) -> int:
        if row < 2:
            return 1
        
        if col == 0:
            return 1
        
        if col == row:
            return 1
        
        if (row, col) not in self.cache.keys():
            self.cache[(row, col)] = self._generate(row - 1, col - 1) + self._generate(row - 1, col)
        
        return self.cache[(row, col)]

