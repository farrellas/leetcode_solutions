class Node:
    def __init__(self, x, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visited = {}
        
    def getNode(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None
        
    def copyRandomList(self, head):
        if head is None:
            return None
        
        oldNode = head
        newNode = Node(oldNode.val, None, None)
        self.visited[oldNode] = newNode
        
        while oldNode:
            newNode.random = self.getNode(oldNode.random)
            newNode.next = self.getNode(oldNode.next)
        
            oldNode, newNode = oldNode.next, newNode.next
        
        return self.visited[head]