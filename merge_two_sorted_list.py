from common import *


def merge_two_lists1(l1: ListNode, l2: ListNode) -> []:
    q = []
    while l1 and l2:
        if l1.val > l2.val:
            q.append(l2.val)
            l2 = l2.next
        else:
            q.append(l1.val)
            l1 = l1.next

    while l1:
        q.append(l1.val)
        l1 = l1.next

    while l2:
        q.append(l2.val)
        l2 = l2.next

    return q


def merge_two_lists2(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1

    if l1:
        l1.next = merge_two_lists2(l1.next, l2)

    return l1


if __name__ == "__main__":
    l1 = get_linked_list([1, 2, 4])
    l2 = get_linked_list([1, 3, 4])
    # print(merge_two_lists1(l1, l2))

    print_linked_list(merge_two_lists2(l1, l2))
