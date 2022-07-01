class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        freshCount = 0
        minutes = 0
        
        q = collections.deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshCount += 1
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    
        while q:
            i, j, minute = q.popleft()
            if i > 0 and grid[i-1][j] == 1:
                freshCount -= 1
                grid[i-1][j] = 2
                q.append((i-1, j, minute+1))
            if i < m-1 and grid[i+1][j] == 1:
                freshCount -= 1
                grid[i+1][j] = 2
                q.append((i+1, j, minute+1))
            if j > 0 and grid[i][j-1] == 1:
                freshCount -= 1
                grid[i][j-1] = 2
                q.append((i, j-1, minute+1))
            if j < n-1 and grid[i][j+1] == 1:
                freshCount -= 1
                grid[i][j+1] = 2
                q.append((i, j+1, minute+1))
            minutes = max(minutes, minute)
            
        return minutes if freshCount == 0 else -1