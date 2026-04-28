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
        dummy = ListNode(0)
        curr = dummy
        while nums != []:
            newNode = ListNode(heapq.heappop(nums), None)
            curr.next = newNode
            curr = curr.next
        return dummy.next    