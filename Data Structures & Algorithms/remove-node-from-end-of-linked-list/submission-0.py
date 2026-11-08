# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        lenthg = 0
        curr = head
        while curr:
            lenthg+=1
            curr = curr.next

        node_to_remove = lenthg - n
        dummy = ListNode(0, head) 
        curr = dummy
        for x in range(node_to_remove):
            curr = curr.next

        curr.next = curr.next.next

        return dummy.next

        




        