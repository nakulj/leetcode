# Definition for singly-linked list.
from typing import Iterator


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def it(node: ListNode | None) -> Iterator[ListNode]:
    while node is not None:
        yield node
        node = node.next


def llist(it: Iterator[ListNode]) -> ListNode | None:
    head = next(it, None)
    if head is None:
        return None
    tail = head
    for node in it:
        tail.next = node
        tail = node
    return head


def pop_max(head: ListNode | None) -> Tuple[ListNode | None, ListNode | None]:
    if head is None:
        return None, None
    if head.next is None:
        return head, None
    max(
        ((parent, node) for parent, node in zip(it(head), it(head.next))),
        key=lambda parent_node: parent_node[1].val,
    )


class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        pass
