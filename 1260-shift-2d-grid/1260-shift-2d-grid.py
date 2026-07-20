class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        # Flatten to 1D
        flat = [grid[i][j] for i in range(m) for j in range(n)]
        
        # Rotate by k
        k = k % len(flat)
        flat = flat[-k:] + flat[:-k]
        
        # Reshape back to 2D
        return [[flat[i * n + j] for j in range(n)] for i in range(m)]