# 10장 데크, 우선순위 큐

*641. Design Circular Deque*

- https://leetcode.com/problems/design-circular-deque

다음 연산을 제공하는 원형 데크를 디자인 하라.

```
Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

- MyCircularDeque(k): Constructor, set the size of the deque to be k.
- insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
- insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
- deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
- deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
- getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
- getRear(): Gets the last item from Deque. If the deque is empty, return -1.
- isEmpty(): Checks whether Deque is empty or not. 
- isFull(): Checks whether Deque is full or not.
```

### 책 풀이

- add : 이미 있는 노드를 찢어내고 그 사이에 새로운 노드 new를 삽입
- del : 오른 오른 쪽에 있는 노드와 head, tail을 연결 해서 삭제

![0](https://user-images.githubusercontent.com/30167661/107145794-59060400-6987-11eb-91cf-4712515dafed.jpeg)

```python
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head
        
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new
    
    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True
        

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True
        

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True
    
    def getFront(self) -> int:
        return self.head.right.val if self.len else -1


    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1
        
    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k
```

*23. Merge k Sorted Lists*

- https://leetcode.com/problems/merge-k-sorted-lists/

Example 1
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

Example 2

```
Input: lists = []
Output: []
```

Example 3:

```
Input: lists = [[]]
Output: []
```

### 내 풀이

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 성능 Runtiume : 100 ms /  Memory : 18.3 MB
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        sub_list = []

        # list와 linked-list를 돌면서 sub_list에 값만 모음
        for i in lists:
            while i:
                sub_list.append(int(i.val))
                i = i.next
        
        # 내장함수를 통해 sort
        sub_list = list(sorted(sub_list))
        
        result_list = None
        pre_node = None
        cur_node = None
        
        # 새로운 linked-list를 만들어서 return
        for i in range(len(sub_list)):
            if i == 0:
                result_list = ListNode(sub_list[i])
                pre_node = result_list
            else:
                pre_node.next = ListNode(sub_list[i])
                pre_node = pre_node.next
        
        return result_list
```

### 책 풀

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 성능 Runtiume : 96 ms /  Memory : 18.1 MB
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []
        
        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                
        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]
            
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
                
        return root.next
```

### PriorityQueue
- 어떤한 특정 조건에 따라 우선순위가 가장 높은 요소가 추출되는 자료형
- heapq를 사용
- lock을 제공하여 thread-safty class 이다.

### heapq
- 이진트리 기반의 최소 힙 자료구조
- 데이터 삽입시 힙의 공식에따른 정렬을 유지한다. -> 부모노드보다 큰 상태, 느슨한 정렬
- 가장 작은값은 항상 index: 0 에 위치한다.

### python GIL
- 파이썬의 멀티쓰레딩

```
파이썬에서 쓰레드을 여러 개 생성한다고 해서 여러 개의 쓰레드가 동시에 실행되는 
것은 아니다. 정확히 말하자면 두 개의 쓰레드가 동시해 실행되는 것처럼 보일 뿐, 
특정 시점에서는 여러 개의 쓰레드 중 하나의 쓰레드만 실행된다.
```

- 왜?
```
파이썬은 객체를 reference count를 통해 관리한다. 
예를 들어, 객체를 참조하는 다른 객체 또는 위치가 늘어날수록 해당 객체의 reference count는 증감하게 되며, 
reference count가 0이 되면 객체는 메모리에서 해제된다. 
이것이 바로 파이썬의 가비지 콜렉터 (Garbage Collector: GC)  기능이다.
그런데 멀티 쓰레딩 환경에서 각 쓰레드가 특정 객체를 사용한다면 어떻게 될까? 
C++이나 자바라면 특정 변수에 대해서만 직접 동기화 처리를 해주면 되겠지만, 
파이썬은 객체의 메모리를 관리하는 방법의 특성 상 모든 객체에 일일이 락을 걸어야만 
제대로 reference count가 가능할 것이다. 
즉, 모든 객체가 크리티컬 섹션이 되어 버리는 대참사가 발생하게 된다. 
```

![lock](https://user-images.githubusercontent.com/30167661/107145809-6cb16a80-6987-11eb-8bf4-963e182a93d1.png)

