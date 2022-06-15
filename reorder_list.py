# my solution
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        forward = head
        backward = head
        stack = []
        visited = set()
        while backward:
            stack.append(backward)
            backward = backward.next
            
        while forward.next not in visited:
            backward = stack.pop()
            visited.add(forward)
            visited.add(backward)
            nextNode = forward.next
            forward.next = backward
            backward.next = nextNode
            forward = nextNode
        forward.next = None

# 2 pointer
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node = head
        stack = []
        while node:
            stack.append(node)
            node = node.next
        l, r = 0, len(stack)-1
        while l < r:
            stack[l].next = stack[r]
            stack[r].next = stack[l+1]
            l += 1
            r -= 1
        stack[l].next = None
        
# find middle, reverse second half, merge two
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = fast = head
        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse
        prev, node = None, slow
        while node:
            node.next, prev, node = prev, node, node.next
        # merge two
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next