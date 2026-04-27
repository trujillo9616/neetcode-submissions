class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = 0
    
        def dfs(r, c):
            if r < 0 or r > n - 1 or c < 0 or c > m - 1 or grid[r][c] == '0':
                return 
            
            grid[r][c] = '0'

            for dx, dy in directions:
                dfs(r + dx, c + dy)


        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)
        
        return res
