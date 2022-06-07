def repeatedSubstringPattern(s):
    for i in range(len(s)//2, 0, -1):
        if len(s) % i == 0:
            if s == s[:i]*(len(s)//i):
                return True
    return False

def repeatedSubstringPattern(s):
        i = 1
        while i <= len(s) / 2:
            substring = s[:i]
            if len(s) % i != 0:
                i+=1
                continue
            divisor = int(len(s) / i)
            if substring * divisor == s:
                return True
            i+=1
        return False