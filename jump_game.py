class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        maxReachableIndex = 0
        for i in range(len(nums)):
            if i > maxReachableIndex:
                return False
            maxReachableIndex = max(maxReachableIndex, i + nums[i])
        return maxReachableIndex >= n