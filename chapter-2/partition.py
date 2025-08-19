"""
2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x. The partition element x can appear anywhere inthe "right partition"; it does not need to appear between the left and right partitions.
EXAMPLE:
Input: 3->5->8->5->10->2->1 [partition = 5]
Output: 3->1->2->10->5->5->8
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

    def print_list(self) -> None:
        curr = self.head
        while curr:
            print(f"{curr.val}->", end = '')
            curr = curr.next
        print()

def partition(node: Optional[Node], x: int) -> Optional[Node]:
    head: Optional[Node] = node
    tail: Optional[Node] = node

    while node:
        next = node.next
        if node.val < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next

    tail.next = None
    return head


if __name__ == '__main__':
    ll = LinkedList()
    for n in [3, 5, 8, 5, 10, 2, 1]:
        ll.append(n)

    ll.print_list()
    ll.head = partition(ll.head, 5);
    ll.print_list()
