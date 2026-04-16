'''

2487. Remove Nodes From Linked List

You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.
Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(arr: list):
    head = ListNode(arr[0], None)
    prev = head
    for item in arr[1:]:
        node = ListNode(item, None)
        if prev is not None:
            prev.next = node
        prev = node
    return head


def traverse(l: ListNode):
    while l:
        print(l.val)
        l=l.next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prior, header = None, None
        curr = head
        while curr:
            new = curr.next
            while new and new.val <= curr.val:
                new = new.next
            if not header:
                header = curr
            if prior:
                prior.next = new
            prior = curr
            curr = new
        return header


head = [1,1,1,1]
head = build_linked_list(head)
sol = Solution()
l=sol.removeNodes(head)
traverse(l)
