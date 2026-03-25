# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        #traverse both lists
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            #sum current digits +carry

            total = val1 + val2 + carry
            carry = total // 10 #update carry
            digit = total % 10 #current node's digit


            #add new node to result
            current.next = ListNode(digit)
            current = current.next

            # move to next nodes if available
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next #Return head of the new list

        
        