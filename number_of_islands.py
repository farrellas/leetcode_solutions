class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for d in directions:
                    r, c = row + d[0], col + d[1]
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        visited.add((r, c))
                        q.append((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    visited.add((r, c))
                    islands += 1
                    bfs(r, c)
        
        return islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for row in grid]
        
        islandCount = 0
        stack = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    islandCount += 1
                    stack.append((i, j))
                
                while stack:
                    x, y = stack.pop()
                    visited[x][y] = True
                    
                    if x > 0 and grid[x-1][y] == "1" and not visited[x-1][y]:
                        stack.append((x-1, y))
                    if y > 0 and grid[x][y-1] == "1" and not visited[x][y-1]:
                        stack.append((x, y-1))
                    if x < len(grid)-1 and grid[x+1][y] == "1" and not visited[x+1][y]:
                        stack.append((x+1, y))
                    if y < len(grid[0])-1 and grid[x][y+1] == "1" and not visited[x][y+1]:
                        stack.append((x, y+1))
        
        return islandCount