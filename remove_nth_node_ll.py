# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        slow = head
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        q = collections.deque()
        curr = head
        if not head.next:
            head.val = ""
            return head
        while curr:
            q.append(curr)
            if len(q) > n+1:
                q.popleft()
            curr = curr.next
        if len(q) == n:
            head = head.next
            return head
        q[0].next = q[1].next
        return head