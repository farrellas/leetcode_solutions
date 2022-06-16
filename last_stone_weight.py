class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1 and heap[0] != 0:
            big = heapq.heappop(heap)
            small = heapq.heappop(heap)
            heapq.heappush(heap, big - small)
        return -heap[0]

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            bisect.insort(stones, stones.pop() - stones.pop())
        return stones[0]