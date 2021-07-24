import sys
sys.path.insert(0, '.')
from pai_util.ch8.singly_linked_list import get_test_node, ListNode, print_list_node
# https://leetcode.com/problems/swap-nodes-in-pairs/
"""
Given a linked list, swap every two adjacent nodes and return its head.

Constraints:
- The number of nodes in the list is in the range [0, 100].
- 0 <= Node.val <= 100

Follow up: 
Can you solve the problem without modifying the values in the list's nodes? 
(i.e., Only nodes themselves may be changed.)

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    문제 정리:
    - 연결 리스트 받아서
    - 모든 두 인접한 노드를 스왑
    - 그 헤드를 반환
    예제:
    1 -> 2 -> 3 -> 4
    2 -> 1 -> 3 -> 4
    (X)2 -> 3 -> 1 -> 4
        - 2와 1을 스왑했으니, 3과 4를 스왑
    (O)2 -> 1 -> 4 -> 3
    """
    def first(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        node_curr = head
        # 1. 반복: 두 개씩 스왑하므로, 현재의 다음 노드가 있는 동안 반복
        while node_curr.next:
            # 2. 노드의 스왑: 값만 바꾸면 되지 않을까?
            node_curr.val, node_curr.next.val = node_curr.next.val, node_curr.val
            # 3. 현재 노드는 다다음 노드로 변경
            if node_curr.next.next:
                node_curr = node_curr.next.next
            else:
                break
        
        return head

    """
    값이 아닌 노드 자체를 변경
    1 -> 2 -> 3 -> 4
        - 다음 노드는 1 -> 3 -> 4로 만들고
        - 2를 앞으로 땡기고
        - 2의 next에 1 -> 3 -> 4를 붙이고
        - 3부터 시작하도록 node_curr를 변경
    1 -> 2 -> 3:
        - 다음 노드는? 3
        - 2 -> 1 -> 3
    """
    # 실패
    def second(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # 1. 반복: 두 개씩 스왑하므로, 현재의 다음 노드가 있는 동안 반복
        # ListNode는 Python Object로 같은 메모리 주소를 가리킨다(by reference)
        # node_curr에는 head에 대한 `주소` 저장
        node_curr = head
        while node_curr and node_curr.next:
            # 2. 스왑
            # - 현재 노드 임시 저장
            tmp = node_curr
            # - 다음 노드를 현재 노드로
            node_nnext = tmp.next.next
            node_curr = tmp.next
            # - `이전 현재 노드`를 다음 노드로
            node_curr.next = tmp
            # - `이전 다음 노드`의 다다음 노드가 있었다면, `현재 다음 노드`의 다음 노드로 치환
            node_curr.next.next = node_nnext
            node_curr = node_curr.next.next

        return head

    # 책 풀이
    def third(self, head: ListNode) -> ListNode:
        # root: 풀이에서 head가 계속 변경되므로, root.next로 결과 값을 반환한다
        # prev: 다음 비교를 위해 두 칸씩 이동시킬 변수
        root = prev = ListNode(None, head)
        
        # head = 1 -> 2 -> 3 -> 4
        while head and head.next:
            # tmp: 값이 실제로 스왑되는 변수
            # 한 쌍에서 다음 노드를 앞으로 끌어 올린다
            # tmp = 2 -> 3 -> 4
            tmp = head.next
            # 다다음 노드를 원래 head의 다음 노드로 할당한다
            # tmp.next = 3 -> 4
            # head = 1 -> 3 -> 4
            head.next = tmp.next
            # 앞으로 끌어 올려진 `이전의 다음 노드`에 head를 붙인다
            # tmp.next = 1 -> 3 -> 4
            # tmp = 2 -> 1 -> 3 -> 4
            tmp.next = head

            # prev = None -> 1 -> 2 -> 3 -> 4
            # prev = None -> 2 -> 1 -> 3 -> 4
            prev.next = tmp

            # head = 3 -> 4
            head = head.next
            # prev = 1 -> 3 -> 4
            prev = prev.next.next
        
        return root.next

    # 재귀 풀이 방식. 가장 끝에서부터 스왑하면서 올라온다
    def fourth(self, head: ListNode) -> ListNode:
        # p = 2
        #   tmp = 4 -> 3 -> None
        #       head = 1 -> 4 -> 3 -> None
        #           p = 2 -> 1 -> 4 -> 3 -> None
        #  2 -> 1 -> 4 -> 3
        if head and head.next:
            # p는 우선 다음 값으로 할당하고
            p = head.next
            # 스왑된 값을 리턴 받는다
            tmp = self.fourth(p.next)
            # 스왑된 tmp를 head의 다음 값에 넣고
            head.next = tmp
            # 헤드를 앞서 스왑된 p의 다음 값에 넣는다
            p.next = head

            return p

        return head

    def swapPairs(self, head: ListNode) -> ListNode:
        ans = None

        return ans


s = Solution()
head = get_test_node([1, 2, 3, 4])
# head = get_test_node([1, 2, 3])
# head = get_test_node([1, 2])
# head = get_test_node([1])
# head = get_test_node([])
print_list_node(s.fourth(head))
