# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class NodeRetriever:
            def __init__(self,node):
                self.node=node
            # __lt__ allows to compare the nodes
            def __lt__(self,other):
                return self.node.val<other.node.val
        newhead=temp=ListNode(0)
        heap=[]
        # put heads of all lists in the min_heap (default is min_heap)
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,NodeRetriever(lists[i]))
        
        # iterates through all nodes(n) in lists 
        while heap:
            # retrieved the node
            # heappop takes log k time where k is the length of lists
            min_node=heapq.heappop(heap)

            temp.next=min_node.node
            temp=temp.next

            # updating pointer of node retrieved
            if min_node.node.next:
                heapq.heappush(heap,NodeRetriever(min_node.node.next))

        return newhead.next

        # t(n)=o(nlogk)
        # s(n)=o(k)
        # n is total number of nodes in lists and length of 'lists' is k
