# DFS recursive

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        childrenDepths = [self.maxDepth(child) for child in root.children]
        d = 0
        if childrenDepths:
            d = max(childrenDepths)
        return 1 + d

# BFS

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        q = collections.deque([(root, 1)])
        d = 1
        while q:
            node, level = q.popleft()
            d = max(d, level)
            for child in node.children:
                q.append((child, level + 1))
        return d