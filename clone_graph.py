class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        clones = {}
        
        def clone(node):
            if node in clones:
                return clones[node]
            
            copy = Node(node.val)
            clones[node] = copy
            
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy
        
        return clone(node) if node else None
        


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        clones = {}
        q = collections.deque([node])
        
        clones[node.val] = Node(node.val)
        
        while q:
            currentNode = q.popleft()
            
            for neighbor in currentNode.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)
                clones[currentNode.val].neighbors.append(clones[neighbor.val])
                
        return clones[node.val]