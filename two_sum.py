def twoSum(nums, target):
    nums_sorted = sorted(nums)
    left = 0
    right = len(nums) - 1
    output = [0, 0]

    while right > left:
        if nums_sorted[right] + nums_sorted[left] == target:
            break
        elif nums_sorted[right] + nums_sorted[left] < target:
            left += 1
        else:
            right -= 1

    if nums_sorted[left] == nums_sorted[right]:
        output[0] = nums.index(nums_sorted[left])
        nums[output[0]] = "x"
        output[1] = nums.index(nums_sorted[right])
        return output

    output[0] = nums.index(nums_sorted[left])
    output[1] = nums.index(nums_sorted[right])
    
    return output



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            if target - nums[i] in hashtable:
                return [hashtable[target-nums[i]], i]
            else:
                hashtable[nums[i]] = i