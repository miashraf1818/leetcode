from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Step 1: Multi-source BFS to compute distance from nearest thief for every cell
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        
        # Step 2: Binary search on the answer (safeness factor)
        def canReach(minSafe):
            if dist[0][0] < minSafe or dist[n-1][n-1] < minSafe:
                return False
            visited = [[False] * n for _ in range(n)]
            queue = deque([(0, 0)])
            visited[0][0] = True
            while queue:
                r, c = queue.popleft()
                if r == n-1 and c == n-1:
                    return True
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and dist[nr][nc] >= minSafe:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            return False
        
        lo, hi = 0, n * 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if canReach(mid):
                lo = mid
            else:
                hi = mid - 1
        
        return lo