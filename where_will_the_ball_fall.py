class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        def dfs(i, j):
            if i == len(grid):
                return j
            if j == 0 and grid[i][j] == -1:
                return -1
            if j == len(grid[0])-1 and grid[i][j] == 1:
                return -1
            if grid[i][j] == 1 and grid[i][j+1] == -1:
                return -1
            if grid[i][j] == -1 and grid[i][j-1] == 1:
                return -1
            if grid[i][j] == 1:
                return dfs(i+1, j+1)
            if grid[i][j] == -1:
                return dfs(i+1, j-1)
        
        output = []
        for j in range(len(grid[0])):
            output.append(dfs(0, j))
        return output

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        def dfs(i):
            for j in range(m):
                i2 = i + grid[j][i]
                if i2 < 0 or i2 >= n or grid[j][i2] != grid[j][i]:
                    return -1
                i = i2
            return i
        return list(map(dfs, range(n)))