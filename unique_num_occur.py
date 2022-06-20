class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = collections.Counter(arr)
        countSet = set(counts.values())
        return len(counts.values()) == len(countSet)


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = collections.Counter(arr)
        countSet = set()
        for num in counts.values():
            if num in countSet:
                return False
            countSet.add(num)
        return True