class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, h = 0 , len(matrix) - 1
        idx = 0
        
        while l <= h:
            m = (l + h) // 2
            if matrix[m][0] <= target:
                idx = m
            if matrix[m][0] <= target:
                l = m + 1
            else:
                h = m - 1
        return self.binSearch(matrix[idx], target)
        
        
    def binSearch(self, lst, target):
        l, h = 0, len(lst) - 1
        
        while l <= h:
            m = (l + h) // 2
            if lst[m] == target:
                return True
            elif lst[m] > target:
                h = m - 1
            else:
                l = m + 1
        return False