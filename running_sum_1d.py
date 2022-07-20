class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [0] * (len(nums))
        for i in range(len(nums)):
            if i > 0:
                output[i] = output[i-1] + nums[i]
            else:
                output[i] += nums[i]
        return output

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums