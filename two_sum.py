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


test1 = [2,7,11,15]
target1 = 9
test2 = [3,2,4]
target2 = 6

print(twoSum(test1, target1))
print(twoSum(test2, target2))
print(twoSum([3,3], 6))
print(twoSum([3,2,3], 6))


