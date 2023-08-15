from common import *


def swap_in_pairs1(head: ListNode) -> ListNode:
    node = head
    stack = []

    while node:
        stack.append(node)
        node = node.next

    prev, carry = None, None
    i = 0
    while stack:
        i = len(stack)
        node = stack.pop()

        if i % 2 == 1:
            if prev:
                prev.next = node
            else:
                prev = node

            if carry:
                node.next = carry
            else:
                node.next = None
        else:
            carry, prev = prev, node

    return prev


def swap_in_pairs2(head: ListNode) -> ListNode:
    cur = head

    while cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        if cur.next.next:
            cur = cur.next.next
        else:
            break

    return head


if __name__ == "__main__":
    print_linked_list(swap_in_pairs2(get_linked_list([1, 2, 3, 4, 5, 6, 7])))
