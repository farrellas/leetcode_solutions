class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 1
        hashset = set()
        hashset.add(fruits[0])
        output = 1
        
        while r < len(fruits):
            hashset.add(fruits[r])
            if len(hashset) > 2:
                hashset.clear()
                hashset.add(fruits[r])
                l = r-1
                hashset.add(fruits[l])
                while True:
                    l -= 1
                    if fruits[l] not in hashset:
                        l += 1
                        r += 1
                        break
            else:
                output = max(output, (r - l) + 1)
                r += 1
        
        return output