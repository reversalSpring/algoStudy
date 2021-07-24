# 8장 연결리스트

## 19. 역순 연결 리스트 II

- https://leetcode.com/problems/reverse-linked-list-ii/

>**92. Reverse Linked List II** (Medium)
>
>Reverse a linked list from position *m* to *n*. Do it in one-pass.
>
>**Note:** 1 ≤ *m* ≤ *n* ≤ length of list.
>
>**Example:**
>
>```
>Input: 1->2->3->4->5->NULL, m = 2, n = 4
>Output: 1->4->3->2->5->NULL
>```



### 1) 반복 구조로 노드 뒤집기

- `start`는 변경이 필요한 2의 바로 앞 지점인 1을 가리키게 함
- `end`는 `start.next`인 2로 지정
- `head`보다 앞에 `root`를 위치시킨다. - `root.next`로 최종결과 리턴
- 반복하면서 노드 차례대로 뒤집기

![image](https://user-images.githubusercontent.com/19264527/106380455-b3d2b500-63f5-11eb-8a39-2758af49a566.png)

```python
# Runtime 20 ms / Memory 14.4 MB
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
      # 예외 처리
      if not head or m == n:
        return head
      
      root = start = ListNode(None)
      root.next = head
      
      # start, end 지정
      for _ in range(m - 1):
        start = start.next
      end = start.next
      
      # 반복하면서 노드 차례대로 뒤집기
      for _ in range(n - m):
        # 다중 할당 처리
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
        
      return root.next
```


