from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # BFS with state (row, col, remaining_health)
        queue = deque([(0, 0, health - grid[0][0])])
        visited = {}
        visited[(0, 0)] = health - grid[0][0]
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while queue:
            r, c, hp = queue.popleft()
            
            if hp <= 0:
                continue
                
            if r == m-1 and c == n-1:
                return True
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_hp = hp - grid[nr][nc]
                    if new_hp > 0 and visited.get((nr, nc), -1) < new_hp:
                        visited[(nr, nc)] = new_hp
                        queue.append((nr, nc, new_hp))
        
        return False