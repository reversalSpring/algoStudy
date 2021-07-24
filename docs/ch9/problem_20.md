# 9장 스택, 큐

- 스택 - 후입선출 / LIFO (Last-In-First-Out)
- 큐 - 선입선출 / FIFO (First-InFirst-Out)
- Python의 리스트는 스택과 큐의 모든 연산을 지원
- 다만, 리스트는 배열로 구현되어있어 큐의 연산을 수행하기에는 효율적이지 않기 때문에, **데크(Deque)** 자료형을 사용해야 좋은 성능을 낼 수 있다.

  

## 스택 (Stack)

- `push()` : 요소를 컬렉션에 추가한다.
- `pop()` : 아직 제거되지 않은 가장 최근에 삽입된 요소를 제거한다.

  

### 연결 리스트를 이용한 스택 ADT 구현

- 물리 메모리 상에는 순서와 관계 없이 여기저기에 무작위로 배치되고 포인터로 가리키도록 구현

- 연결리스트를 담을 Node 클래스 정의

  ```python
  class Node:
    def __init__(self, item, next):
      self.item = item # 노드의 값
      self.next = next # 노드를 가리키는 포인터
  ```

- 스택의 연산 `push()`, `pop()` 을 담은 `Stack` 클래스

  ```python
  class Stack:
    def __init(self):
      self.last = None
      
    # 가장 마지막 값을 next로 지정하고, 포인터인 last는 마지막으로 이동
    def push(self, item):
      self.last = Node(item, self.last)
      
    # 가장 마지막 아이템을 끄집어내고 last 포인터를 한 칸 앞으로 전진.
    def pop(self):
      item = self.last.item
      self.last = self.last.next
      return item
  ```

- 스택 사용

  ```python
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  stack.push(4)
  stack.push(5)
  
  for _ in range(5):
    print(stack.pop())
  
  5
  4
  3
  2
  1
  ```

  

## 20. 유효한 괄호

- https://leetcode.com/problems/valid-parentheses/

>**20. Valid Parentheses** (Easy)
>
>Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
>
>An input string is valid if:
>
>1. Open brackets must be closed by the same type of brackets.
>2. Open brackets must be closed in the correct order.
>
>**Example 1:**
>
>```
>Input: s = "()"
>Output: true
>```
>
>**Example 2:**
>
>```
>Input: s = "()[]{}"
>Output: true
>```
>
>**Example 3:**
>
>```
>Input: s = "(]"
>Output: false
>```
>
>**Example 4:**
>
>```
>Input: s = "([)]"
>Output: false
>```
>
>**Example 5:**
>
>```
>Input: s = "{[]}"
>Output: true
>```
>
>**Constraints:**
>
>- `1 <= s.length <= 104`
>- `s` consists of parentheses only `'()[]{}'`.

### 내 풀이

```python
# Runtime 20 ms / Memory 14.3 MB
class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(', '[', '{']
        close_bracket = {'(':')', '{':'}', '[':']'}
        stack = []
        
        for ch in s:
            if ch in open_brackets:
                stack.append(close_bracket[ch])
            elif len(stack) <= 0 or stack.pop() is not ch:
                    return False
                
        if len(stack) > 0:
            return False
        else:
            return True
```

  

### 1) 스택 일치 여부 판별

- 스택은 파이썬의 동적 배열 구현인 리스트를 사용 (푸시와 팝이 O(1)에 동작)
- `(`, `[`, `{`  - 스택에 푸시 (Push)
- `)`, `]`, `}` - 스택에서 팝(Pop)한 결과가 매핑 테이블 결과와 매칭되는지 확인

```python
# Runtime 32 ms / Memory 14.2 MB
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
          ')':'(',
          '}':'{',
          ']':'[',
        }
        
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                    return False
        
        # 스택이 비어있는지 여부 확인
        return len(stack) == 0
```
