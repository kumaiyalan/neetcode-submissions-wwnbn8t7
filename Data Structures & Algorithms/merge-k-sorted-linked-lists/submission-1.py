# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        for head in lists:
            while head:
                nums.append(head.val)
                head = head.next
        heapq.heapify(nums)
        merged = ListNode(0)
        head = merged
        while nums != []:
            merged.next = ListNode(heapq.heappop(nums), None)
            merged = merged.next
        return head.next    