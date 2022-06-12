from collections import deque

def levelOrder(root):
    if root is None:
        return []
    levels = []
    q = deque([root])
    level = 0
    
    while q:
        levels.append([])
        length = len(q)
        
        for i in range(length):
            node = q.popleft()
            levels[level].append(node.val)
        
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        level += 1
        
        
    return levels