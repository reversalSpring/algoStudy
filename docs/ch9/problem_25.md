# 9장 스택, 큐
## <a name='TOC'>목차</a>
0. [목차](#TOC)
1. [큐를 이용한 스택 구현(Implement Stack using Queues)](#ISuQ)
2. [스택을 이용한 큐 구현(Implemnt Queue using Stacks)](#IQuS)
2. [두 정렬 리스트의 병합(Merge Two Sorted Lists)](#mtsl)

## <a name='ISuQ'>#225 - 큐를 이용한 스택 구현(Implement Stack using Queues)</a> 
### (1) 내 풀이
```python
from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        return self.queue.pop()
        

    def top(self) -> int:
        if self.queue:
            return self.queue[len(self.queue)-1]
        else:
            return None        


    def empty(self) -> bool:
        if self.top() is None:
            return True
        else:
            return False
```
- Point
  - deque를 사용
- 평가
  - Runtime: **28 ms, faster than 82.15%** of Python3 online submissions for Implement Stack using Queues.
  - Memory Usage: **14.3 MB, less than 47.70%** of Python3 online submissions for Implement Stack using Queues.

### (2) 책의 해설
```python3
class MyStack:
    def __init__(self):
        self.q = collections.deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        

    def pop(self) -> int:
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[0]   


    def empty(self) -> bool:
        return len(self.q) == 0
```
- Point
  - 요소를 append 한 다음, 그 요소를 맨 앞으로 보내는 식으로 전체를 재정렬함
  - 결과적으로 '맨 앞 요소 == 가장 마지막에 넣은 요소' 가 된다.
  - 결국 popleft()를 해도 결과는 LIFO가 되는 것
  
### (3) queue를 두 개 활용한 풀이 [(출처)](https://leetcode.com/problems/implement-stack-using-queues/discuss/381976/Python-solutions)
```python3
from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self._top = None
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        self._top = x  # 현 시점에서 마지막으로 넣은 요소가 _top
        # 책 풀이와는 달리 넣기만 해서는 popleft()시 FIFO 상태

    def pop(self) -> int:
        while len(self.q1) > 1:  # 요소가 두 개 이상일 때부터 착실하게 하나씩 빼낸다.
            self._top = self.q1.popleft()  # 결국 q1에 남은 건 둘 중에 더 나중에 들어온 요소이므로
            self.q2.append(self._top)  # q2에는 더 먼저 들어온 요소가 하나씩 붙고
        result = self.q1.popleft()  # 어쨌든 LIFO 가 된다.
        self.q1, self.q2 = self.q2, self.q1  # (q1에 요소가 둘 이상이었을 떄) q1은 가장 나중에 들어온 요소가 담긴 채로, q2는 빈 채로 끝난다.
        return result
        

    def top(self) -> int:
        return self._top


    def empty(self) -> bool:
        return len(self.q1) == 0
```
- Point
  - Streamlining the push operation to O(1) and trading off pop to O(n).
  

## <a name='IQuS'>#232 - 스택을 이용한 큐 구현(Implemnt Queue using Stacks)</a>
### (1) 내 풀이 - 1
```python3
class MyQueue:
    # Stack : LIFO
    # Queue : FIFO
    # 스택으로 FIFO 구조를 만들어라.

    def __init__(self):
        self.s1 = list()  # LIFO
        self.s2 = list()  # s1을 뒤집은 형태
        self.out = None
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        self.s2 = list(reversed(self.s1))
        

    def pop(self) -> int:
        self.out = self.peek()
        self.s2.remove(self.peek())
        self.s1.remove(self.s1[0])
        return self.out
        

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        else:
            return None
        

    def empty(self) -> bool:
        return self.peek() == None
```
- 생각의 흐름
  - stack 두 개를 사용 + 기본 함수만 사용하라는 조건을 만족하고자 노력함
  - 하지만 stack 하나만 쓰는 게 더 깔끔할듯.
- 평가
  - Runtime: **32 ms, faster than 55.19%** of Python3 online submissions for Implement Queue using Stacks.
  - Memory Usage: **14.1 MB, less than 98.89%** of Python3 online submissions for Implement Queue using Stacks.

### (2) 내 풀이 - 2
```python3
class MyQueue:

    def __init__(self):
        self.s1 = list()
        self.out = None
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:
        self.out = self.peek()
        self.s1.remove(self.peek())
        return self.out
        

    def peek(self) -> int:
        if self.s1:
            return list(reversed(self.s1))[-1]
        else:
            return None
        

    def empty(self) -> bool:
        return self.peek() == None
```
- Point
  - stack 하나만 사용한 풀이
- 평가
  - Runtime: **32 ms, faster than 55.19%** of Python3 online submissions for Implement Queue using Stacks.
  - Memory Usage: **14.3 MB, less than 75.67%** of Python3 online submissions for Implement Queue using Stacks.
  

### (3) 책 풀이
```python3
class MyQueue:
    # Stack : LIFO
    # Queue : FIFO
    # 스택으로 FIFO 구조를 만들어라.

    def __init__(self):
        self.input = []
        self.output = []
        

    def push(self, x: int) -> None:
        self.input.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.output.pop()  # peek()에서의 로직때문에 pop()을 해도 먼저 들어온 요소가 먼저 나간다.
        

    def peek(self) -> int:
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())  # input은 비우고, output은 가장 먼저 들어온 요소가 제일 뒤에 있게 된다.
        return self.output[-1]
        

    def empty(self) -> bool:
        return self.input == [] and self.output == []
```
- Point
  - 스택 2개 사용 (스택의 연산만을 사용해서 풀기 위해서는 2개의 스택이 필요)
  - pop()과 peek()은 결국 같은 데이터를 빼 내므로, pop()을 할 때 peek()을 호출하고 거기서 재입력하도록 구현

## <a name='DCQ'>#622 - 원형 큐 디자인(Design Circular Queue)</a>
### (1) 내 풀이
```python3
class MyCircularQueue:
    # 원형큐는 FIFO 선입선출
    # 마지막이 처음과 이어진다.

    def __init__(self, k: int):
        self.q = collections.deque(maxlen=k)
        self.size = k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q.append(value)
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q.popleft()
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[0]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[-1]
        

    def isEmpty(self) -> bool:
        return len(self.q) == 0
        

    def isFull(self) -> bool:
        return len(self.q) == self.size
```
- Point
  - 원형 큐로도 사용할 수 있는 collections 모듈의 deque를 사용
- 평가
  - Runtime: **68 ms, faster than 74.95%** of Python3 online submissions for Design Circular Queue.
  - Memory Usage: **14.8 MB, less than 50.31%** of Python3 online submissions for Design Circular Queue.

### (2) 책의 해설
```python3
class MyCircularQueue:
    # 원형큐는 FIFO 선입선출
    # 마지막이 처음과 이어진다.

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0  # front 포인터
        self.p2 = 0  # rear 포인터
        

    def enQueue(self, value: int) -> bool:
        # rear 포인터 이동
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        # front 포인터 이동
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True
        

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]
        

    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]
        

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None
        

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None
```
- Point
  - 배열과 두 포인터를 이용
