# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def it(n:ListNode|None):
    while n is not None:
        yield n.val
        n = n.next

def merge_it(a:ListNode|None, b:ListNode|None)->ListNode|None:
    if a is None or b is None:




class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       for  
