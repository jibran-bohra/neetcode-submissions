from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r >= m or c >= n:
                return
            if r< 0 or c<0:
                return
                
            if grid[r][c] == "0":
                return
                
            if (r, c) in visited:
                return 

            visited.add((r,c))

            dfs(r, c + 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)

        visited = set()
        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count += 1
                    dfs(r,c)
        
        return count