class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(i, cur, total):
            if total == target:
                result.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
            
        dfs(0, [], 0)
        return result