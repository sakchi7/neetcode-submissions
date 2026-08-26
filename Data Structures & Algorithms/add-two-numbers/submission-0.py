# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = curr = ListNode()
        while l1 and l2:
            sum = (carry + l1.val + l2.val)%10
            carry = (carry + l1.val + l2.val)//10
            curr.next = ListNode(sum)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        temp = l1 or l2
        while temp:
            sum = (carry + temp.val)%10
            carry = (carry + temp.val)//10
            curr.next = ListNode(sum)
            curr = curr.next
            temp = temp.next
        if carry:
            curr.next = ListNode(carry)
            curr = curr.next
        return head.next

        