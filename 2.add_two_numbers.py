# Definition for singly-linked list.
from typing import Iterator, Optional
from itertools import zip_longest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def it(head: ListNode | None):
    while head is not None:
        yield head.val
        head = head.next


def llist(it: Iterator) -> ListNode | None:
    head = ListNode(next(it))
    tail = head
    for v in it:
        tail.next = ListNode(v)
        tail = tail.next
    return head


def add(a: ListNode | None, b: ListNode | None):
    carry = 0
    for av, bv in zip_longest(it(a), it(b), fillvalue=0):
        s = av + bv + carry
        yield s % 10
        carry = s // 10
    if carry > 0:
        yield carry


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        return llist(add(l1, l2))
