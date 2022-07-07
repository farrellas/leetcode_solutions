# rotates by each "pixel"
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                temp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = temp
                
# transposes across diagonal and then mirrors
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)
        
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    
    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


# using pointers to control swaps
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        
        while l < r:
            top, bottom = l, r
            for i in range(r - l):
                temp = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = temp
                
            l += 1
            r -= 1

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        
        while l < r:
            top, bottom = l, r
            for i in range(r - l):
                matrix[top][l + i], matrix[bottom - i][l], matrix[bottom][r - i], matrix[top + i][r] = matrix[bottom - i][l], matrix[bottom][r - i], matrix[top + i][r], matrix[top][l + i]
                
            l += 1
            r -= 1