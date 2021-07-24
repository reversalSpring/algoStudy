# Runtime 68ms / Memory 24.6MB


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        li = []

        while head is not None:
            li.append(head.val)
            head = head.next

        return li == li[::-1]

