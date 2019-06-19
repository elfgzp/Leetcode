from collections import deque
class Solution:
    di = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        start = tuple(start)
        queue = deque([start])
        visited = {start}
        
        rows = len(maze)
        cols = len(maze[0])
        
        x, y = destination
        while queue:
            cur = queue.popleft()
            r0, c0 = cur
                        
            if r0 == x and c0 == y:
                return True
            
            
            for i, drc in enumerate(self.di):
                dr, dc = drc
                
                r = r0
                c = c0
                while 0 <= r + dr < rows and 0 <= c + dc < cols and maze[r + dr][c + dc] == 0:
                    r += dr
                    c += dc
                    
                if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0 and (r, c) not in visited:
                    queue.append((r, c))
                    visited.add((r, c))
        
        return False

