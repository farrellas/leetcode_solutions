def diStringMatch(s):
    perm = []
    low = 0
    high = len(s)
    counter = 0
    
    while counter < len(s):
        if s[counter] == "I":
            perm.append(low)
            low += 1
        elif s[counter] == "D":
            perm.append(high)
            high -= 1
        counter += 1
    perm.append(low)
    return perm