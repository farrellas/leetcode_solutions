class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            head = ListNode(list1.val, None)
            list1 = list1.next
        else:
            head = ListNode(list2.val, None)
            list2 = list2.next
        node = head
        while list1 or list2:
            if list1 is None:
                node.next = ListNode(list2.val, None)
                node, list2 = node.next, list2.next
                continue
            if list2 is None:
                node.next = ListNode(list1.val, None)
                node, list1 = node.next, list1.next
                continue
            if list1.val <= list2.val:
                node.next = ListNode(list1.val, None)
                node, list1 = node.next, list1.next
            else:
                node.next = ListNode(list2.val, None)
                node, list2 = node.next, list2.next
                
        return head