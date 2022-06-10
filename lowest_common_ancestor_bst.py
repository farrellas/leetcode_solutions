def lowestCommonAncestor(root, p, q):
    if p == root or q == root:
        return root
    while True:
        if p.val > root.val and q.val > root.val:
            root = root.right
        elif p.val < root.val and q.val < root.val:
            root = root.left
        else:
            return root