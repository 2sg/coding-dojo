# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # dummy node
        dummy = cur = ListNode(0)
        carry = 0
        
        # loop through the lists while there are still nodes left
        while l1 or l2 or carry:
            # get the values of the current nodes
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            # calculate new digit and carry
            carry, val = divmod(v1 + v2 + carry, 10)
            
            # add new node to the result
            cur.next = ListNode(val)
            cur = cur.next

        # return the result list
        return dummy.next