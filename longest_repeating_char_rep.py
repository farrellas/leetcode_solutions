class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        chars = {}
        output = 0
        chars[s[0]] = 1
        
        while r < len(s):
            currentChar = s[r]
            chars[currentChar] = chars.get(currentChar, 0) + 1
            currentStreak = r - l + 1
            if max(chars.values()) + k < currentStreak:
                chars[s[l]] -= 1
                l += 1
                r += 1
            else:
                output = max(output, currentStreak)
                r += 1
        return output