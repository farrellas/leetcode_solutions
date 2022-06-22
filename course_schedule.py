class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preReqMap[crs].append(pre)
        
        # visited set
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if preReqMap[crs] == []:
                return True
            
            visited.add(crs)
            for pre in preReqMap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            preReqMap[crs] = []
            return True
            
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True