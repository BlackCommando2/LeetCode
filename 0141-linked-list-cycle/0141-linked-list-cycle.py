# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        curr = head
        after = head
        while after and after.next:
            curr = curr.next
            after = after.next.next
            if curr == after:
                return True
        return False