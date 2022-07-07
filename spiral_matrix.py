class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        i, j = 0, 0
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        total = len(matrix) * len(matrix[0])
        
        while len(output) < total:
            for i in range(l, r + 1):
                output.append(matrix[t][i])
            for j in range(t + 1, b + 1):
                output.append(matrix[j][r])
                
            if t != b:
                for i in range(r - 1, l - 1, -1):
                    output.append(matrix[b][i])
            if l != r:
                for j in range(b - 1, t, -1):
                    output.append(matrix[j][l])
            
            t += 1
            r -= 1
            b -= 1
            l += 1
        return output