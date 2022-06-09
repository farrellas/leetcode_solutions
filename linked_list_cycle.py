def hasCycle(head):
    if head is None:
        return False
    visited = {head}
    curr = head
    while curr.next:
        if curr.next in visited:
            return True
        visited.add(curr)
        curr = curr.next
    return False