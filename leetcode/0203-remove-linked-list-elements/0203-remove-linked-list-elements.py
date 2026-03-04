# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy=ListNode(0)
        dummy.next=head
        curr = dummy
        prev = dummy
        while curr.next != None:
            prev = curr
            curr = curr.next
            if curr.val == val:
                prev.next = curr.next
                curr = prev
        return dummy.next 


      
       
       