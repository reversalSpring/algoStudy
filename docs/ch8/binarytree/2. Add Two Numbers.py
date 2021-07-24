# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = curr = ListNode(0)
        plus = 0
        num = 0

        while l1 or l2:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            sum += plus

            if sum > 9:
                sum %= 10
                plus = 1
            else:
                plus =0

            curr.next = ListNode(sum)
            curr = curr.next

        if plus != 0:
            curr.next = ListNode(plus)

        head = head.next

        return head