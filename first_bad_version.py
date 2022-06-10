def firstBadVersion(n):
        l = 1
        r = n
        while l < r:
            mid = int(l + (r - l) / 2)
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        
        return l