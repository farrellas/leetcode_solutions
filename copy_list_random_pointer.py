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

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        node = head
        while node:
            new = Node(node.val, None, None)
            new.next = node.next
            node.next = new
            node = new.next
        
        node = head
        while node:
            node.next.random = node.random.next if node.random else None
            node = node.next.next
            
        oldList = head
        newList = head.next
        newHead = head.next
        while oldList:
            oldList.next = oldList.next.next
            newList.next = newList.next.next if newList.next else None
            oldList = oldList.next
            newList = newList.next
            
        return newHead

class Solution:
    def __init__(self):
        self.visited = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        if head in self.visited:
            return self.visited[head]
        
        node = Node(head.val, None, None)
        self.visited[head] = node
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node