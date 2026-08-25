# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenList = 0
        curr = head
        while curr:
            lenList += 1
            curr = curr.next
        
        index = lenList - n
        if index == 0:
            head = head.next
            return head
        lenList = 0
        curr = head
        prev = None
        while curr:
            if index == lenList:
                prev.next = curr.next
            lenList += 1
            prev = curr
            curr = curr.next
        return head