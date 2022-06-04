def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) < 2:
        return len(s)
    maximum = 1
    letters = set()
    l = 0
    r = 1
    letters.add(s[l])
    while r < len(s):
        print(l, r, letters)
        if len(letters) < maximum:
            l += 1
            r += 1
            letters = set(s[l:r+1])
            
        elif s[r] in letters:
            maximum = max(len(letters), maximum)
            l += 1
            r = l + maximum + 1
            letters = set(s[l:r])
                
        else:
            letters.add(s[r])
            r += 1
            
    maximum = max(len(letters), maximum)
    
    return maximum