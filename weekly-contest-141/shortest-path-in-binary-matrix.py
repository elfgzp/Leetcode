from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        queue = deque([((0,0), 1)])
        visited = {(0, 0)}
        
        drs = [-1, 0, 1]
        dcs = [-1, 0, 1]
        
        while queue:
            cur, step = queue.popleft()
            r0, c0 = cur
            
            if r0 == n - 1 and c0 == n - 1:
                return step
            
            for dr in drs:
                for dc in dcs:
                    r, c = r0 + dr, c0 + dc
                    
                    if 0 <= r < n and 0 <= c < n and grid[r][c] == 0 and (r, c) not in visited:
                        visited.add((r, c))
                        queue.append(((r, c), step + 1))
        
        return -1
        
