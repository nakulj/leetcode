# Definition for singly-linked list.
from typing import Iterator


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def filtered_it(head:ListNode|None,val:int)->Iterator[ListNode]:
    while head is not None:
        if head.val != val:
            yield head
        head = head.next




class Solution:
    def removeElements(self, head:ListNode|None, val: int) ->ListNode|None:
        it = filtered_it(head,val)
        head = next(it,None)
        if head is None:
            return None
        tail = head
        for node in it:
            tail.next = node
            tail = node
        tail.next = None
        return head
        
