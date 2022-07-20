class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if not root:
            return output
        d = collections.defaultdict(list)
        q = collections.deque([[root, 0]])
        
        while q:
            node, level = q.popleft()
            d[level].append(node.val)
            if node.left:
                q.append([node.left, level+1])
            if node.right:
                q.append([node.right, level+1])
                
        for i in range(len(d)):
            output.append(d[i][-1])
        
        return output

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if not root:
            return output
        
        def dfs(node, level):
            if level == len(output):
                output.append(node.val)
            for child in (node.right, node.left):
                if child:
                    dfs(child, level + 1)
                    
        dfs(root, 0)
        return output