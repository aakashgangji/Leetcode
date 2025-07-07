from typing import List, Optional

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists or len(lists) == 0:
        return None
    while len(lists) > 1:
        mergedList = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if (i+1) < len(lists) else None
            mergedList.append(mergelists(l1, l2))
        lists = mergedList
    return lists[0]

def mergelists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return dummy.next

# Helper function: Convert a Python list to a linked list
def array_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function: Convert a linked list to a Python list
def linked_list_to_array(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Input: list of Python lists
input_lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
linked_lists = [array_to_linked_list(lst) for lst in input_lists]  # Convert to ListNode objects

# Merge and print
merged_head = mergeKLists(linked_lists)
print(linked_list_to_array(merged_head))
