# Runtime 32ms / Memory 14.3MB


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        first, last, result = l1, l2, l1

        if l1 is None:
            result = l2
        elif l2 is not None and l1.val > l2.val:
            result = l2
            first = l2
            last = l1

        while first is not None and last is not None:
            if first.val <= last.val:
                if first.next is None:
                    first.next = last
                    first, last = None, None
                elif last.val < first.next.val:
                    temp = first.next
                    first.next = last
                    last = temp
                    first = first.next
                else:
                    first = first.next
        return result

