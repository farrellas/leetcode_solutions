# DFS recursive

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# BFS

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = collections.deque([(root, 1)])
        d = 1
        while q:
            node, level = q.popleft()
            d = max(d, level)
            if node.right:
                q.append((node.right, d+1))
            if node.left:
                q.append((node.left, d+1))
                
        return d

