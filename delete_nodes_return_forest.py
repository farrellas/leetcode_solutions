# original solution

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        newRoots = []
        q = collections.deque([(root, None)])
        if root.val not in to_delete:
            newRoots.append(root)
        while q:
            node, parent = q.popleft()
            
            if node.val in to_delete:
                if node in newRoots:
                    newRoots.remove(node)
                if parent:
                    if parent.right and parent.right.val == node.val:
                        parent.right = None
                    else:
                        parent.left = None
                if node.left:
                    q.append([node.left, None])
                    newRoots.append(node.left)
                    node.left = None
                if node.right:
                    q.append([node.right, None])
                    newRoots.append(node.right)
                    node.right = None

            else:
                if node.left:
                    q.append([node.left, node])
                if node.right:
                    q.append([node.right, node])
                
        return newRoots

# optimized solution

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delSet = set(to_delete)
        newRoots = []
        q = collections.deque([(root, False)])
        
        while q:
            node, hasParent = q.popleft()
            
            if not hasParent and node.val not in delSet:
                newRoots.append(node)
                
            hasParent = not node.val in delSet
            
            if node.left:
                q.append((node.left, hasParent))
                if node.left.val in delSet:
                    node.left = None
            if node.right:
                q.append((node.right, hasParent))
                if node.right.val in delSet:
                    node.right = None
                    
        return newRoots