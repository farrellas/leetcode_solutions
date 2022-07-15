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

# backtracking
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(tmp, start, end, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    tmp.append(candidates[i])
                    backtrack(tmp, i, end, target - candidates[i])
                    tmp.pop()
        ans = [] 
        candidates.sort(reverse= True)
        backtrack([], 0, len(candidates), target)
        return ans