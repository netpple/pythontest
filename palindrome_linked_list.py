import collections
from common import *


def is_palindrome1(string: str) -> bool:
    result = string.replace("->", "")
    return result == result[::-1]


def is_palindrome2(head: ListNode) -> bool:
    node = head
    string = ""
    while node:
        string += str(node.val)
        node = node.next

    return string == string[::-1]


def is_palindrome3(head: ListNode) -> bool:
    node = head
    q = []

    while node:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


def is_palindrome4(head: ListNode) -> bool:
    node = head
    q = collections.deque()

    while node:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


def is_palindrome5(head: ListNode) -> bool:
    node = head
    tail = head.prev

    while node:
        if node.val != tail.val:
            return False
        node = node.next
        tail = tail.prev

    return True


def is_palindrome6(head: ListNode) -> bool:
    slow: ListNode = head
    fast: ListNode = head
    rev: ListNode = None

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    while rev:
        if rev.val != slow.val:
            return False
        rev, slow = rev.next, slow.next

    return True


if __name__ == "__main__":
    # print(is_palindrome1("1->2->3->2->1"))

    head = get_linked_list([1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1])
    # print(is_palindrome2(head))
    # print(is_palindrome3(head))
    # print(is_palindrome4(head))
    print(is_palindrome5(head))
    print(is_palindrome6(head))
