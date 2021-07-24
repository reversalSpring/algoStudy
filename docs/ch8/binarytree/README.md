## 15. 역순 연결 리스

- https://leetcode.com/problems/reverse-linked-list

**206. Reverse Linked List**
Reverse a singly linked list.

**Example 1:**

```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

### 풀이 및 코드

1. 이전, 지금, 다음 노드를 변수로 저장하여 각각의 포인트를 반대로 연

##개인 코드
```python
        # Runtime: 40 ms
        # Memory Usage: 15.7 MB

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
```

##다 폴이
```python
        # 어떤 능력자의 코드
        # prev = None
        # while head:
        #     head.next, prev, head = prev, head, head.next
        # return prev

        # 책에서 recursive
        node, prev = head, None
        while node:
           next, node.next = node.next, prev
           prev, node = node, next
        
        return prev
```

## 16. 두 수의 덧셈

- https://leetcode.com/problems/add-two-numbers/

**2. Add Two Numbers**

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

**Example 1**
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

**Example 2**
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3**
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

### 풀이 및 코드

1. l1과 l2의 노드가 있을 경우 값을 더하고 다음 노드로 변경
2. 이전 자리올림수 더하기
3. 기존 노드와 연결
4. 마지막 올림수가 있다면 마지막에 추가

##개인 코드
```python
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
```

##다른 폴이
```python
# 연결 리스트 뒤집기
node, prev = head, None
while node:
   next, node.next = node.next, prev
   prev, node = node, next

return prev

# 연결 리스트를 파이썬 리스트로 변환
def toList(self, node: ListNode) -> ListNode:
    list: List = []
    while node:
        list.append(node.val())
        node = node.next
    return list

# 파이썬 리스트를 연결 리스트로 변환
def toReversedLinkedList(self, result: ListNode) -> ListNode:
    prev: Listnode = None
    for r in result:
        node = ListNode(r)
        node.next = prev
        prev = node
    return node

# 두 연결 리스트의 덧셈
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    a = self.toList(self.reverseList(l1))
    b = self.toList(self.reverseList(l2))

    resultStr = int(''.join(str(e) for e in a)) + \
                int(''.join(str(e) for e in b))

# 최종 계산 결과 연결 리스트 변환
     return self.toRversedLinkedList(str(resultStr))
```