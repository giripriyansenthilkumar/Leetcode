class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        mx=0
        n=len(grid)
        m=len(grid[0])
        vis=[[False]*m for _ in range(n)]

        def backtrack(i,j):
            nonlocal mx
            if i<0 or j<0 or i>=n or j>=m:
                return 0
            if vis[i][j] or grid[i][j]==0:
                # mx=max(mx,c)
                return 0
            c=1
            vis[i][j]=True
            c+=backtrack(i,j+1)
            c+=backtrack(i+1,j)
            c+=backtrack(i,j-1)
            c+=backtrack(i-1,j)
            return c

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not vis[i][j]:
                    c=backtrack(i,j)
                    mx=max(mx,c)
        return mx