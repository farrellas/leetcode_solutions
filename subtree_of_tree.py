# my solution using bfs style
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = collections.deque([root])
        
        def isSameTree(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and \
                isSameTree(p.right, q.right)
            return False
        
        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                newRoot = node
                if isSameTree(node, subRoot):
                    return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False

# full recursive

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)
        return False

# using hashset to compare subtrees - fast, but high memory
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs_set(root, hash_set):
            if not root:
                return 'X'
            
            key = ",".join([str(root.val), dfs_set(root.left, hash_set), dfs_set(root.right, hash_set)])
            hash_set.add(key)
            
            return key

        hash_set = set()
        dfs_set(root, hash_set)
        subtree_key = dfs_set(subRoot, set())
        
        return subtree_key in hash_set