class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maximum = 0
        while l < r:
            lower = min(height[l], height[r])
            maximum = max(((r-l) * lower), maximum)
            if height[l] == lower:
                l += 1
            else:
                r -= 1
        return maximum

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maximum = 0
        while l < r:
            if height[l] <= height[r]:
                curr = (r-l) * height[l]
                l += 1
            else:
                curr = (r-l) * height[r]
                r -= 1
            if curr > maximum: maximum = curr
        return maximum