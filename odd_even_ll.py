class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odds = head
        evens = evenHead = head.next
        while evens and evens.next:
            odds.next = evens.next
            odds = odds.next
            evens.next = odds.next
            evens = evens.next   
        odds.next = evenHead
        return head

# faster
class Solution(object):
    def oddEvenList(self, head):
        if head is None: return None
        if head.next is None: return head
        o = head
        e = o.next
        ehead = e
        while e.next is not None:
            
            o.next = e.next
            e.next = e.next.next
            
            o = o.next
            e = e.next
            if e is None: break
                
        o.next = ehead
        return head