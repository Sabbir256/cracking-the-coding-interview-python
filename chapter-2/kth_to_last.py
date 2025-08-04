"""
2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list
"""

from typing import Optional

class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Optional[Node] = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr and curr.next:
            curr = curr.next
        curr.next = new_node

# SOLUTION 1: print the node value
def print_kth_to_last(head: Optional[Node], k: int) -> int:
    if head is None:
        return 0

    index = 1 + print_kth_to_last(head.next, k)
    if index == k:
        print(f"{k}th to the last node is {head.val}")
    return index

# SOLUTION 2: return the Kth node
def kth_to_last(head: Optional[Node], k: int) -> Optional[Node]:
    idx: list = [0] # list behaves as pass by reference
    return _kth_to_last(head, k, idx)

def _kth_to_last(head: Optional[Node], k: int, idx: list) -> Optional[Node]:
    if not head:
        return None
    node = _kth_to_last(head.next, k, idx)
    idx[0] += 1
    if idx[0] == k:
        return head
    return node

if __name__ == '__main__':
    ll = LinkedList()
    for n in [4, 5, 3, 10, 1, 7]:
        ll.append(n)

    print_kth_to_last(ll.head, 3)

    node = kth_to_last(ll.head, 3)
    assert node is not None
    assert node.val == 10


