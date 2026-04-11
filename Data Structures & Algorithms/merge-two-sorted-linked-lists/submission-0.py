# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        
        holder = 0
        holder2 = 0

        if list1.val > list2.val: #list 1 will start smaller or equal
            holder = list1
            list1 = list2
            list2 = holder

        head = list1

        while list1 is not None and list1.next is not None and list2 is not None: #pull to list1
            if list1.next.val > list2.val:
                holder = list1.next
                list1.next = list2
                holder2 = list2.next
                list1 = list1.next
                list1.next = holder
                list2 = holder2
            else:
                list1 = list1.next

        if list2 is not None:
            list1.next = list2
        return head
