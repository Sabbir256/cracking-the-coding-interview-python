"""
2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

from typing import Optional

class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.next: Optional[Node] = None

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def append(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return

        curr: Node = self.head
        while curr and curr.next:
            curr = curr.next
        curr.next = new_node

    def print(self) -> None:
        curr = self.head
        while curr is not None:
            print(curr.val, end=' ')
            curr = curr.next

# SOLUTION 1 - use set/hash
def remove_dups(head: Optional[Node]) -> None:
    seen = set()
    prev: Optional[Node] = None
    curr: Optional[Node] = head

    while curr is not None:
        if curr.val in seen and prev:
            prev.next = curr.next
        else:
            seen.add(curr.val)
            prev = curr
        curr = curr.next

def delete_dups(head: Optional[Node]) -> None:
    curr = head
    while curr is not None:
        runner = curr
        while runner.next is not None:
            if runner.next.val == curr.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next

if __name__ == '__main__':
    arr: list[int] = [5, 7, 2, 1, 5, 4, 3, 3, 7, 8]
    ll = LinkedList()

    for n in arr:
        ll.append(n)

    # remove_dups(ll.head)
    delete_dups(ll.head)
    ll.print()





