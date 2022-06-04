def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    sCounts = {}
    tCounts = {}
    
    for i in range(len(s)):
        sCounts[s[i]] = sCounts.get(s[i], 0) + 1
        tCounts[t[i]] = tCounts.get(t[i], 0) + 1
    for letter in sCounts.keys():
        if tCounts.get(letter, 0) == 0:
            return False
        if sCounts[letter] != tCounts[letter]:
            return False
    return True


def isAnagram(s, t):
    return sorted(list(s)) == sorted(list(t))
        