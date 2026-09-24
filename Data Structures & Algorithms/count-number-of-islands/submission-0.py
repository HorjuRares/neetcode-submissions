class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if not (0 <= i < len(grid)): return
            if not (0 <= j < len(grid[0])): return
            if grid[i][j] == '0': return

            grid[i][j] = '0'

            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            

        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != '0':
                    dfs(i, j)
                    num_islands += 1

        return num_islands
        