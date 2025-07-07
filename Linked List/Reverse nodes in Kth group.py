# You are given the head of a singly linked list head and a positive integer k.
# You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.
# Return the modified list after reversing the nodes in each group of k.
# You are only allowed to modify the nodes' next pointers, not the values of the nodes.
# Example 1:
# Input: head = [1,2,3,4,5,6], k = 3
# Output: [3,2,1,6,5,4]
# Example 2:
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]

from typing import List
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy=ListNode(0,head)
        groupPrev=dummy

        while True:
            kth=self.getkth(groupPrev,k)
            if not kth:
                break
            groupNext=kth.next
            prev,cur=kth.next,groupPrev.next
            while cur!=groupNext:
                tmp=cur.next
                cur.next=prev
                prev=cur
                cur=tmp
            tmp=groupPrev.next
            groupPrev.next=kth
            groupPrev=tmp
        return dummy.next



    def getkth(self,cur,k):
        while cur and k>0:
            cur=cur.next
            k-=1
        return cur
    
def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

# Creating the linked list: 1 -> 2 -> 3 -> 4 -> 5
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

head = node1
k = 3
result_head = Solution().reverseKGroup(head, k)
print_linked_list(result_head)  # Output: [3, 2, 1, 4, 5]