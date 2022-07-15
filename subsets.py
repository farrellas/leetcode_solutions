class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end, tmp):
            output.append(tmp[:])
            for i in range(start, end):
                tmp.append(nums[i])
                backtrack(i+1, end, tmp)
                tmp.pop()
        
        
        output = []
        backtrack(0, len(nums), [])
        return output