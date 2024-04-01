# Definition for singly-linked list.
from typing import Iterator


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def it(head:ListNode|None)->Iterator[ListNode]:
    while head is not None:
        yield head
        head = head.next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
