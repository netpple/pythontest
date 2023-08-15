from common import *


def reverse_linked_list1(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        node, prev = next, node

    return prev


def reverse_linked_list2(prev: ListNode, node: ListNode) -> ListNode:
    next, node.next = node.next, prev
    # reverse
    parent = reverse_linked_list2(node, next) if next else node

    return parent


if __name__ == "__main__":
    result = reverse_linked_list1(get_linked_list([1, 2, 3, 4, 5]))
    print_linked_list(result)
