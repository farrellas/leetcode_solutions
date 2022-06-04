# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1, l2):
    num1 = self.findListNum(l1)
    num2 = self.findListNum(l2)
    total = num1 + num2
    return self.convertToLL(total)

def findListNum(self, ll):
    output = ''
    while ll.next:
        output += str(ll.val)
        ll = ll.next
    output += str(ll.val)
    output = output[::-1]
    return int(output)

def convertToLL(self, input):
    ll = []
    str_input = str(input)
    i = len(str_input) - 1
    while i >= 0:
        if i == 0:
            value = int(str_input[i])
            ll.append(ListNode(value))
        else:
            value = int(str_input[i])
            next_node = ll
            ll.append(ListNode(value, next_node))
        i -= 1
    return ll

