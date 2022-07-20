# recursive
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, lo, hi):
            if not node:
                return True
            if node.val <= lo or node.val >= hi:
                return False
            return check(node.left, lo, node.val) and check(node.right, node.val, hi)
        return check(root, float('-inf'), float('inf'))

# recursive inorder
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node: return True
            if not check(node.left):
                return False
            if node.val <= self.last:
                return False
            self.last = node.val
            return check(node.right)
            
        self.last = float('-inf')
        return check(root)
