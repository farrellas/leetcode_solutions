# my BFS solution. unexplicably won't pass, but passes on vscode and pythontutor...
import collections
class Solution:
    def networkDelayTime(self, times, n, k) -> int:
        seenTimes = {}
        edges = collections.defaultdict(list)
        
        for edge in times:
            edges[edge[0]].append((edge[1], edge[2]))
            
        q = collections.deque([[k, 0]])
        seenTimes[k] = 0
        while q:
            location, time = q.popleft()
            seenTimes[location] = min(seenTimes.get(location, float('inf')), time)
            while edges[location]:
                edge = edges[location].pop()
                q.append([edge[0], edge[1] + time])
            
        minTime = 0
        for location in seenTimes:
            minTime = max(minTime, seenTimes[location])
        
        return minTime if len(seenTimes) == n else -1
    
times = [[2,1,47],[3,5,46],[4,1,6],[5,4,7],[4,5,19],[3,2,18],[1,2,0],[5,1,25],[2,5,58]]
test = Solution()
print(test.networkDelayTime(times, 5, 3))

# SPFA
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        seenTimes = [float('inf') for _ in range(n)]
        seenTimes[k-1] = 0
        weight = collections.defaultdict(dict)
        for frm, to, time in times:
            weight[frm][to] = time
        q = collections.deque([k])
        while q:
            frm = q.popleft()
            for to in weight[frm]:
                if seenTimes[frm-1] + weight[frm][to] < seenTimes[to-1]:
                    seenTimes[to-1] = seenTimes[frm-1] + weight[frm][to]
                    q.append(to)
        return max(seenTimes) if max(seenTimes) < float('inf') else -1

# Bellman-Ford algo - pretty fast after adding the flag. also uses minimal space compared to others
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        seenTimes = [float('inf') for _ in range(n)]
        seenTimes[k-1] = 0
        for _ in range(n):
            flag = 1
            for frm, to, time in times:
                if seenTimes[frm-1] + time < seenTimes[to-1]:
                    seenTimes[to-1] = seenTimes[frm-1] + time
                    flag = 0
            if flag:
                break
        return max(seenTimes) if max(seenTimes) < float('inf') else -1

# dijkstra's - efficient version
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, c in times:
            graph[src].append((dst, c)) 
        
        
        queue = [(0, k)] #(cost, node)
        visited = set()
        max_cost = 0
            
        while queue:
            
            #Always pop the min value
            cost, node = heapq.heappop(queue)
            
            if node in visited:
                continue
                
            visited.add(node)
            
            max_cost = max(max_cost, cost)

            neighbours = graph[node]
            
            for neighbour in neighbours:
                
                new_node, new_cost = neighbour
                
                if new_node not in visited:
                    
                    curr_cost =  cost + new_cost
                    
                    heapq.heappush(queue, (curr_cost, new_node))
        

        return max_cost if len(visited) == n else -1