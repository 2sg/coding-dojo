# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Traverse list1 until we reach node a-1
        prev = None
        curr = list1
        for _ in range(a):
            prev = curr
            curr = curr.next

        # Connect node a-1 to head of list2
        prev.next = list2

        # Traverse list2 until its end
        while list2.next:
            list2 = list2.next

        # Traverse list1 until node b+1
        for _ in range(b - a + 1):
            curr = curr.next

        # Connect end of list2 to node b+1 of list1
        list2.next = curr

        return list1
