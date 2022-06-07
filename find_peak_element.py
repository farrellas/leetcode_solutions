def findPeakElement(nums):
        if len(nums) < 2:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        
        l = 0
        r = len(nums) - 1
        while r >= l:
            mid = int(l + (r - l)/2)
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                print(nums[mid])
                return mid
            elif nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid - 1
        return mid