class Solution:
    
    def traverse(self, root, output):
        if root is None:
            return output
        output.append(root.val)
        self.traverse(root.left, output)
        self.traverse(root.right, output)
        return output
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.traverse(root, output)
        return output