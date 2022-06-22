class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1, dp2 = 0, 0
        
        for n in nums:
            temp = max(n + dp1, dp2)
            dp1 = dp2
            dp2 = temp
        return dp2