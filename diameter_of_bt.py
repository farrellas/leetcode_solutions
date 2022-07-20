class Solution:
    def __init__(self):
        self.d = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            self.d = max(self.d, l + r)
            
            return max(l, r) + 1
        dfs(root)
        return self.d