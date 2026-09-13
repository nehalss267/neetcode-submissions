# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2
        newHead=None
        temp=None
        if list1 and list2 and list1.val>list2.val:
            newHead=ListNode(list2.val)
            list2=list2.next
        elif list1 and list2 and list1.val<=list2.val:
            newHead=ListNode(list1.val)
            list1=list1.next
        listhead=newHead
        while list1 and list2:
            if list1.val>list2.val:
                temp=ListNode(list2.val)
                newHead.next=temp
                list2=list2.next
            else:
                temp=ListNode(list1.val)
                newHead.next=temp
                list1=list1.next
            newHead=newHead.next
        if list1 and not list2:
            newHead.next=list1
        if list2 and not list1:
            newHead.next=list2
        return listhead


       