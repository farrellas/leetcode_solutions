class Solution:
    def nextClosestTime(self, time: str) -> str:
        lst = [int(time[0]), int(time[1]), int(time[3]), int(time[4])]
        sortedNums = sorted(lst)
        for num in sortedNums:
            if num > lst[3]:
                return f"{lst[0]}{lst[1]}:{lst[2]}{num}"
        for num in sortedNums:
            if lst[2] < num < 6:
                return f"{lst[0]}{lst[1]}:{num}{sortedNums[0]}"
        for num in sortedNums:
            if lst[0] < 2 and num > lst[1]:
                return f"{lst[0]}{num}:{sortedNums[0]}{sortedNums[0]}"
            elif lst[1] < num < 4:
                return f"{lst[0]}{num}:{sortedNums[0]}{sortedNums[0]}"
        for num in sortedNums:
            if lst[0] < 2 and lst[0] < num < 3:
                return f"{num}{sortedNums[0]}:{sortedNums[0]}{sortedNums[0]}"
            
        return f"{lst[0]}{lst[0]}:{lst[0]}{lst[0]}"