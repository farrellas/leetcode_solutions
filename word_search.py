class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(i, j, index):
            board[i][j] = ""
            if index == len(word)-1:
                return True
            if i > 0 and board[i-1][j] == word[index+1]:
                if dfs(i-1, j, index+1):
                    return True
            if j > 0 and board[i][j-1] == word[index+1]:
                if dfs(i, j-1, index+1):
                    return True
            if i < m-1 and board[i+1][j] == word[index+1]:
                if dfs(i+1, j, index+1):
                    return True
            if j < n-1 and board[i][j+1] == word[index+1]:
                if dfs(i, j+1, index+1):
                    return True
            
            board[i][j] = word[index]
            return False
            
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False