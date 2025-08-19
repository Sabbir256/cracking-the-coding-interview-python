"""
2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a single linked list, given only access to that node.

EXAMPLE:
Input: the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
"""

from typing import Optional

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next: Optional[Node] = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, val)->None:
        if self.head is None:
            self.head = Node(val)
            return

        curr = self.head
        while curr and curr.next:
            curr = curr.next
        curr.next = Node(val)

    def print_list(self) -> None:
        curr = self.head
        while curr:
            print(f"{curr.val}->", end='')
            curr = curr.next
        print()

def delete_node(node: Optional[Node]) -> bool:
    if node is None or node.next is None:
        return False

    next: Node = node.next
    node.val = next.val
    node.next = next.next
    return True

if __name__ == '__main__':
    arr = ['a', 'b', 'c', 'd', 'e', 'f']

    ll = LinkedList()
    for c in arr:
        ll.append(c)

    ll.print_list()
    delete_node(ll.head.next.next)
    ll.print_list()
