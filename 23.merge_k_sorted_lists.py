from heapq import heapify, heappop, heappush


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def zip_lists(nodes: list[ListNode]):
    heap = [(node.val, i, node) for i, node in enumerate(nodes)]
    heapify(heap)
    while heap:
        val, i, node = heappop(heap)
        yield val
        if node.next is not None:
            heappush(heap, (node.next.val, i, node.next))


def lst(it) -> ListNode | None:
    v = next(it, None)
    if v is None:
        return None
    head = ListNode(v)
    tail = head
    for v in it:
        tail.next = ListNode(v)
        tail = tail.next
    return head


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        return lst(zip_lists([lst for lst in lists if lst]))
