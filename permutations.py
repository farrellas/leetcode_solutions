class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(first):
            if first == n:
                output.append(nums[:])
            
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
                
        n = len(nums)
        output = []
        backtrack(0)
        return output


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            output.extend(perms)
            nums.append(n)
        
        return output