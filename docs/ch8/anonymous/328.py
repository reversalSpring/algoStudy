import sys
sys.path.insert(0, '.')
from pai_util.ch8.singly_linked_list import get_test_node, ListNode, print_list_node
# https://leetcode.com/problems/odd-even-linked-list/

"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성

Constraints:
- The relative order inside both the even and odd groups should remain as it was in the input.
- The first node is considered odd, the second node even and so on ...
- The length of the linked list is between [0, 10^4].
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    1    2    3    4    5
    1    3    5    2    5
    """
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        # 홀수만 모으기 위한 헤드
        # 1 -> 2 -> 3 -> 4 -> 5
        odd = head
        # 짝수만 모으기 위한 헤드
        # 2 -> 3 -> 4 -> 5
        even = head.next
        even_head = head.next

        while even and even_head:
            # 짝수번째에 다음 홀수번째 값을 할당한다
            # - odd.next = 1 -> 3 -> 4 -> 5
            #   - odd.next = 5
            odd.next = odd.next.next
            # 다음 홀수번째 노드로 이동
            # - odd = 3 -> 4 -> 5
            #   - odd = 5
            odd = odd.next
            # - even = 2 -> 4 -> 5
            #   - even = 4 -> None
            even.next = even.next.next
            # 다음 짝수번째 노드로 이동
            # - even = 4 -> 5
            #   - even = None
            even = even.next

        # 짝수번째 노드만 모은 헤드를 붙인다
        odd.next = even_head

        return head



s = Solution()
head = get_test_node([1, 2, 3, 4, 5])
# head = get_test_node([1, 2, 3])
# head = get_test_node([1, 2])
# head = get_test_node([1])
# head = get_test_node([])
print_list_node(s.oddEvenList(head))