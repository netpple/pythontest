class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def get_linked_list(nums: [int]):
    head: ListNode = None
    node: ListNode = None
    prev: ListNode = None
    for num in nums:
        node = ListNode(num)

        if not prev:
            head = node
        else:
            prev.next = node

        node.prev = prev
        prev = node

    head.prev = node

    return head


def print_linked_list(l: ListNode) -> str:
    string=""
    while l:
        string += str(l.val)
        l = l.next
    print(string)
    return string
