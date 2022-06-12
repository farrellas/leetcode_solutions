class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        stack = []
        node = head
        while node:
            stack.append(node.val)
            node = node.next
        node2 = head
        while node2:
            node2.val = stack.pop()
            node2 = node2.next
            
        return head

