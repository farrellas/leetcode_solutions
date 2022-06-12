class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newList = []
        start, end = newInterval
        i, n = 0, len(intervals)
        
        while i < n and start > intervals[i][0]:
            newList.append(intervals[i])
            i += 1
            
        if len(newList) == 0 or newList[-1][1] < start:
            newList.append(newInterval)
        else:
            newList[-1][1] = max(newList[-1][1], end)
            
        while i < n:
            current = intervals[i]
            i += 1
            
            if newList[-1][1] < current[0]:
                newList.append(current)
            else:
                newList[-1][1] = max(newList[-1][1], current[1])
            
        return newList