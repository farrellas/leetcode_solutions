class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        maximum = 0
        letters = set()
        l = r = 0
        
        while r < len(s):
            rightChar = s[r]
            if rightChar in letters:
                while rightChar in letters:
                    leftChar = s[l]
                    letters.remove(leftChar)
                    l += 1
            letters.add(rightChar)
            maximum = max(maximum, r - l +1)
            r += 1
            
        return maximum