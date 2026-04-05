'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

'''

from typing import Optional


def build_linked_list(arr: list):
    head = ListNode(arr[0], None)
    prev = head
    for item in arr[1:]:
        node = ListNode(item, None)
        if prev is not None:
            prev.next = node
        prev = node
    return head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev


head = [1, 2, 3, 4, 5]
ll = build_linked_list(head)
sol = Solution()
hd = sol.reverseList(ll)
print(hd)
while hd.next:
    print(hd.val)
    hd = hd.next
