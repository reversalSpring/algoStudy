# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # 어떤 능력자의 코드
        # prev = None
        # while head:
        #     head.next, prev, head = prev, head, head.next
        # return prev

        # 책에서 recursive
        # def reverse(node: ListNode, prev: ListNode = None):
        #   if not node:
        #       return prev
        #   next, node.next = node.next, prev
        #   return reverse(next, node)
        # return reverse(head)

        # 책에서 반복 구로조 뒤집기
        # node, prev = head, None
        # while node:
        #    next, node.next = node.next, prev
        #    prev, node = node, next
        #
        # return prev

        if not head:
            return None

        prev = None
        cur = head
        next_node = cur.next

        while next_node:
            cur.next = prev
            prev = cur
            cur = next_node
            next_node = next_node.next

        # 마지막 원소
        cur.next = prev
        prev = cur

        return prev

