
'''
1669. Merge In Between Linked Lists

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        rec = 0
        prev_node, last_node = None, None
        res = list1

        while list1:
            if rec + 1 == a:
                prev_node = list1
            elif rec == b:
                last_node = list1
            list1 = list1.next
            rec += 1
        prev_node.next = list2

        while list2.next != None:
            list2 = list2.next
        list2.next = last_node.next
        return res