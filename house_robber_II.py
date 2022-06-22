class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1, dp2 = 0, 0
        
        for i in range(len(nums)-1):
            temp = max(dp1 + nums[i], dp2)
            dp1 = dp2
            dp2 = temp
        first = dp2
        
        dp1, dp2 = 0, 0
        for i in range(1, len(nums)):
            temp = max(dp1 + nums[i], dp2)
            dp1 = dp2
            dp2 = temp
        second = dp2
            
        return max(first, second)


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
        
    def helper(self, nums):
        dp1, dp2 = 0, 0
        for n in nums:
            temp = max(dp1 + n, dp2)
            dp1, dp2 = dp2, temp
        return dp2