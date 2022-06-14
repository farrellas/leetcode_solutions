class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        stripped_string = ''
        
        for c in s:
            if c.isalnum():
                stripped_string += c.lower()
                
        return stripped_string == stripped_string[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True