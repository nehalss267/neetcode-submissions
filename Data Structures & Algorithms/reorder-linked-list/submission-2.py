# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,head):
        if not head:
            return head
        curr=head
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # find middle
        slow=fast=head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        secHalf=slow
        # if length of linked list is 1, then return else prev=None(fast.next=none so control doen't enter loop)
        prev.next=None
        firstHalf=head
        # reverse 2nd half
        secHalf=self.reverse(secHalf)
        temp=ListNode()
        idx=0
        # merge
        while firstHalf and secHalf:
            if idx%2==0:
                temp.next=firstHalf
                firstHalf=firstHalf.next
            else:
                temp.next=secHalf
                secHalf=secHalf.next
            idx+=1
            temp=temp.next
        temp.next=firstHalf or secHalf
        
