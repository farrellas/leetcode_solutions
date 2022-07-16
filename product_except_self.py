class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        ans[0] = 1
        r = 1
        for i in range(1, len(ans)):
            ans[i] = nums[i-1] * ans[i-1]
        for i in range(len(ans)-1, -1, -1):
            ans[i] = ans[i] * r
            r *= nums[i]
        return ans