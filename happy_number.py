class Solution:
    def __init__(self):
        self.visited = set()
        
    def isHappy(self, n: int) -> bool:
        lst = list(str(n))
        res = 0
        for n in lst:
            n = int(n)
            res += n * n
            if res in self.visited:
                return False
        self.visited.add(res)
        if res == 1:
            return True
        return self.isHappy(res)

# floyds algo
class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(num):
            total = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total += digit ** 2
            return total
        
        slow = n
        fast = getNext(n)
        while fast != 1 and slow != fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))
        return fast == 1