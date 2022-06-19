# O(n) space - this ran faster on LC

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        children = set()
        for node in tree:
            for child in node.children:
                if child not in children:
                    children.add(child)
                
        for node in tree:
            if node and node not in children:
                return node



# O(1) space - this ran slower, but used less space

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        total = 0
        for node in tree:
            total += node.val
            for child in node.children:
                total -= child.val
                
        for node in tree:
            if node.val == total:
                return node

