# heap
class TimeMap:

    def __init__(self):
        self.tm = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        heapq.heappush(self.tm[key], (-timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        for el in self.tm[key]:
            prev = abs(el[0])
            if prev <= timestamp:
                return el[1]
        return ''

# binary search
class TimeMap:

    def __init__(self):
        self.tm = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        lst = self.tm[key]
        l, r = 0, len(lst)
        
        while l < r:
            m = (l + r) // 2
            if lst[m][0] <= timestamp:
                l = m + 1
            else:
                r = m
                
        return "" if r == 0 else lst[r-1][1]