from common import *


def two_sum(l1: ListNode, l2: ListNode) -> ListNode:
    head = tot = None
    p = 0 # 올림수
    while l1 or l2:
        num1, num2 = l1.val if l1 else 0, l2.val if l2 else 0
        sum = num1 + num2 + p
        p = (sum // 10) if sum >= 10 else 0  # 자리올림수

        node = ListNode(sum % 10) # 일의 자리만 저장
        if not tot:
            tot = head = node
        else:
            tot.next = node
            tot = tot.next

        l1 = l1.next if (l1 and l1.next) else None
        l2 = l2.next if (l2 and l2.next) else None

    return head


if __name__ == "__main__":
    print_linked_list(two_sum(get_linked_list([2, 4, 5]), get_linked_list([5, 6, 4, 3, 2])))
