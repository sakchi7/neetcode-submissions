"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        while curr:
            temp = Node(curr.val)
            temp.next = curr.next
            curr.next = temp
            curr = temp.next
        newHead = head.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        curr = head
        while curr:
            temp = curr.next
            curr.next = temp.next
            if temp.next:
                temp.next = temp.next.next
            curr = curr.next
        return newHead