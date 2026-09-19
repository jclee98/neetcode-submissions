# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
init the pointers, prev, curr as the null and head respectively
while the current is not null
    store curr's next to not overwrite
    then you want curr's next to become prev
    prev to become curr
    and curr to become stored next
return prev

'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
