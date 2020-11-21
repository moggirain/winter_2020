# Leetcode 21
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists_iterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        # iterative 
        # TC: O(m+n) SC: O(1)
        dummy = ListNode(None)
        head = dummy 
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next 
            else:
                dummy.next = l2
                l2 = l2.next 
            dummy = dummy.next 
        
        dummy.next = l1 or l2 
        return head.next 

    def mergeTwoLists_recursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        # TC: O(m+n) SC: O(m+n)
        # base case 
        if not l1: return l2 
        if not l2: return l1 
        if l1.val < l2.val:
            l1.next = mergeTwoLists_recursive(l1.next, l2)
            return l1 
        else:
            l2.next = mergeTwoLists_recursive(l2.next, l1)
            



