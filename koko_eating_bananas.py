class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = math.ceil(sum(piles) / h), max(piles)
        
        while l < r:
            m = (l + r) // 2
            hours = 0
            
            for pile in piles:
                hours += math.ceil(pile / m)
            if hours <= h:
                r = m
            else:
                l = m + 1
                
        return r