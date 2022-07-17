# sets
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                if val in rows[r]:
                    return False
                else:
                    rows[r].add(val)
                
                if val in cols[c]:
                    return False
                else:
                    cols[c].add(val)
                    
                box_index = (r // 3) * 3 + (c // 3)
                if val in boxes[box_index]:
                    return False
                else:
                    boxes[box_index].add(val)
        return True

# sets simplified
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r] or val in cols[c] or val in boxes[r//3][c//3]:
                    return False
                    
                rows[r].add(val)
                cols[c].add(val)
                boxes[r//3][c//3].add(val)
        return True

# list with value as index
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0]*9 for _ in range(9)]
        cols = [[0]*9 for _ in range(9)]
        boxes = [[0]*9 for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                val = int(board[r][c])-1
                
                if rows[r][val]:
                    return False
                else:
                    rows[r][val] = 1
                
                if cols[c][val]:
                    return False
                else:
                    cols[c][val] = 1
                    
                box_index = (r // 3) * 3 + (c // 3)
                if boxes[box_index][val]:
                    return False
                else:
                    boxes[box_index][val] = 1
        return True