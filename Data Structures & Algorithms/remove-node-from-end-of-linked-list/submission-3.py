# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        temp=head
        length=0
        while temp:
            length+=1
            temp=temp.next
        # if n==1:
        #     temp=head
        #     while temp.next:
        #         temp=temp.next
        #     temp.next=None
        #     return head
        else:
            n=length-n
            print(length,n)
            if n==0:
                return head.next
            temp=head
            idx=0
            while temp:
                if idx==n-1:
                    temp.next=temp.next.next
                    return head
                print(idx)
                idx+=1
                temp=temp.next
        return head

