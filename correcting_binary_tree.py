import collections

def correctBinaryTree(root):
    visited = {root}
    queue = collections.deque()
    queue.append((root, None))
    while queue:
        currentNode, parent = queue.popleft()
        if currentNode.right in visited:
            if currentNode == parent.right:
                parent.right = None
            else:
                parent.left = None
            return root
        if currentNode.right != None:
            queue.append((currentNode.right, currentNode))
        if currentNode.left != None:
            queue.append((currentNode.left, currentNode))
        visited.add(currentNode)
    return root




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node or (node.right and node.right.val in seen): return
            seen.add(node.val)
            node.right = dfs(node.right)
            node.left = dfs(node.left)
            return node
            
        seen = set()
        return dfs(root)
             
# We can use either DFS or BFS for this. BFS will save some space (same complexity) while DFS is cleaner.

# Complexity
# Time complexity: O(N)
# Space complexity: O(N)

# ======== BFS =========

#         q = [root]
#     	while any(q):
# 		    # Traverse the tree level by level
# 		    temp = []
# 		    for node in q:
# 			    if node.left: temp.append(node.left)
# 			    if node.right: temp.append(node.right)
		
#     		# Check if the invalid node is in temp
# 	    	for node in temp:
# 		    	if node.right in temp:
# 			    	# Find the invalid node's parent
# 				    for parent in q:
# 					    # Remove the invalid node and all of it's children
# 					    if parent.left == node: parent.left = None
# 					    if parent.right == node: parent.right = None
# 				    return root

# 		    q = temp    

