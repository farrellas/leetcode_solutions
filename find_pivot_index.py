class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l, total = 0, sum(nums)
        for i in range(len(nums)):
            if i > 0:
                l += nums[i-1]
            if (l * 2) + nums[i] == total:
                return i
        return -1

