# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        out = head
        while list1 and list2:
            if list1.val<list2.val:
                out.next = list1
                list1 = list1.next
            else:
                out.next = list2
                list2 = list2.next
            out = out.next
        out.next = list1 or list2
        return head.next