class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        h, w = len(grid), len(grid[0])
        
        def bfs(grid, location):
            size = 0
            q = collections.deque([location])
            
            while q:
                i, j = q.popleft()
                
                if grid[i][j] == 1:
                    grid[i][j] = 'X'
                    size += 1
                    if i < h-1 and grid[i+1][j] == 1:
                        q.append((i+1, j))
                    if i > 0 and grid[i-1][j] == 1:
                        q.append((i-1, j))
                    if j < w-1 and grid[i][j+1] == 1:
                        q.append((i, j+1))
                    if j > 0 and grid[i][j-1] == 1:
                        q.append((i, j-1))

            return size
                    
        for y in range(h):
            for x in range(w):
                if grid[y][x] == 1:
                    maxArea = max(maxArea, bfs(grid, (y, x)))
                else:
                    grid[y][x] = 'X'

        return maxArea