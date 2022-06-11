class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.heights = {}
        
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.height(root, 0)
        return self.heights.values()
        
    def height(self, root, level):
        if not root:
            return level
        lh = self.height(root.left, level)
        rh = self.height(root.right, level)
        
        h = max(lh, rh)
        
        self.heights[h] = self.heights.get(h, [])
        self.heights[h].append(root.val)
        return h + 1