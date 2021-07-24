## 60. 삽입 정렬 리스트

- https://leetcode.com/problems/insertion-sort-list/

>**147. Insertion Sort List** (Medium)
>
>Given the `head` of a singly linked list, sort the list using **insertion sort**, and return *the sorted list's head*.
>
>The steps of the **insertion sort** algorithm:
>
>1. Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
>2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
>3. It repeats until no input elements remain.
>
>The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.
>
>![img](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)
>
> 
>
>**Example 1:**
>
>![img](https://assets.leetcode.com/uploads/2021/03/04/sort1linked-list.jpg)
>
>```
>Input: head = [4,2,1,3]
>Output: [1,2,3,4]
>```
>
>**Example 2:**
>
>![img](https://assets.leetcode.com/uploads/2021/03/04/sort2linked-list.jpg)
>
>```
>Input: head = [-1,5,3,4,0]
>Output: [-1,0,3,4,5]
>```
>
> 
>
>**Constraints:**
>
>- The number of nodes in the list is in the range `[1, 5000]`.
>- `-5000 <= Node.val <= 5000`

  

### 1) 삽입 정렬

- 정렬을 해야할 대상(`head`) / 정렬을 끝낸 대상(`cur`), 두 그룹으로 나눠 진행
- 정렬이 되지 않은 부분의 첫번째 값을 정렬된 부분의 올바른 자리에 삽입

![image](https://user-images.githubusercontent.com/19264527/115110780-192b5080-9fb8-11eb-8205-f9c5e3db984f.png)

- 입력값 4 → 2 → 1 → 3, `head`는 루트 노드인 4를 가리킴

![image](https://user-images.githubusercontent.com/19264527/115111740-b25c6600-9fbc-11eb-934f-e1ddc8043dc0.png)

  

- 정렬을 해야할 대상(`head`)이 존재하는 동안 반복
- `cur` 과 `parent` 에 빈 노드 할당
- `cur` 에는 정렬을 끝낸 연결 리스트를 추가해줄 계획. 
- `parent`는 계속 `cur`의 루트를 가리키도록 한다.
- 정렬된 상태인 `cur`과 정렬을 해야할 대상 `head`를 비교하면서 `cur`의 값이 더 작다면 `cur.next`를 이용해 계속 다음으로 이동

```python
cur = parent = ListNode(None)
while head:
    while cur.next and cur.next.val < head.val:
        cur = cur.next
```



- 정렬이 필요한 위치, 즉 `cur`에 삽입될 위치를 찾았다면 `cur` 연결리스트에 추가
  - 찾은 `cur` 위치 다음에 `head` 가  들어감
  - `head.next` 에는 `cur.next` 를 연결해 계속 이어지게 한다.
- 다음번 `head` 는 `head.next` 를 차례로 이어받는다.
- `cur = parent` 를 통해 다시 처음으로 돌아가며 차례대로 다시 반복

```python
cur.next, head.next, head = head, cur.next, head.next
            
cur = parent
```



- 수행시간이 너무 길다 → 최적화 필요

```python
# Runtime 1948 ms / Memory 16.3 MB
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(None)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            
            cur.next, head.next, head = head, cur.next, head.next
            
            cur = parent
        return cur.next
```

  

### 2) 삽입 정렬의 비교 조건 개선

- 1번 풀이는 제대로된 삽입 정렬 풀이가 아니다.
  - 삽입 정렬은 정답 셋과 정답 아닌 셋을 비교할 때, 정답 셋의 가장 **큰 값**부터 **왼쪽 방향**으로 내려가며 스왑되는 위치를 찾아야 한다.
  - 이 문제의 경우 연결리스트이고, 이중 연결리스트도 아니기 때문에 큰 값에서 작은 값까지 거꾸로 거슬러 내려가는게 불가능
  - 매번 가장 작은 값 부터 차례대로 크기 비교를 하는 것은 매우 비효율적



- 다음번 `head`를 비교할 때 정렬된 노드인 `cur`의 처음부터 비교하는 부분 개선 필요
  - 만약 다음번 `head`도 `cur`보다 큰 상태라면 굳이 되돌아가지 않아도 되지 않을까?
  - `cur = parent` 앞에 조건문 추가
    - 다음 번 `head`가 `None`일 수 있기 때문에 존재 여부 확인
    - `cur`과 `head`의 값을 비교해 꼭 필요한 경우에만 되돌아가도록 함
    - `cur.val`이 `head.val`보다 작다면, 그 다음 반복 때 while 구문이 실행되지 않고 바로 교환이 진행됨

```python
if head and cur.val > head.val:
    cur = parent
```



- `cur.val`을 비교할 때 `None` 타입이면 에러가 발생하므로 초기값을 `ListNode(0)`로 할당

```python
# Runtime 176 ms / Memory 16.2 MB
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 초기값 변경
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
                 
            cur.next, head.next, head = head, cur.next, head.next
            
            # 필요한 경우에만 cur 포인터로 돌아가도록 처리
            if head and cur.val > head.val:
                cur = parent
        return parent.next
```

​        

### 실행 시간 비교

- 단 한줄의 조건문으로 기존 대비 10배 이상 성능을 높임

| 풀이 | 방식                       | 실행 시간 |
| ---- | -------------------------- | --------- |
| 1    | 삽입 정렬                  | 1936ms    |
| 2    | 삽입 정렬의 비교 조건 개선 | 180ms     |

​    

## 61. 가장 큰 수

- https://leetcode.com/problems/largest-number/

>**179. Largest Number** (Medium)
>
>Given a list of non-negative integers `nums`, arrange them such that they form the largest number.
>
>**Note:** The result may be very large, so you need to return a string instead of an integer.
>
> 
>
>**Example 1:**
>
>```
>Input: nums = [10,2]
>Output: "210"
>```
>
>**Example 2:**
>
>```
>Input: nums = [3,30,34,5,9]
>Output: "9534330"
>```
>
>**Example 3:**
>
>```
>Input: nums = [1]
>Output: "1"
>```
>
>**Example 4:**
>
>```
>Input: nums = [10]
>Output: "10"
>```
>
>
>
>**Constraints:**
>
>- `1 <= nums.length <= 100`
>- `0 <= nums[i] <= 109`

  

### 1)  삽입 정렬

- 맨 앞에서부터 자릿수 단위로 비교해서 크기 순으로 정렬
  - 9는 30보다 맨 앞자리 수가 더 크므로 9가 더 앞에 와야한다.
  - 930이 큰지 309가 큰지 비교하는 것과 같음
  - `a+b`와 `b+a`를 비교하는 형태로 처리
  - 아래 함수 결과가 `True`이면 위치 변경

```python
def to_swap(n1: int, n2: int) -> bool:
    return str(n1) + str(n2) < str(n2) + str(n1)
```



- 배열로 풀이하는 삽입 정렬을 위한 수도 코드
  - 인덱스를 지정할 수 있어 연결리스트와는 코드가 많이 달라진다.

```python
i ← 1
while i < length(A)
    j ← i
    while j > 0 and A[j - 1] > A[j]
        swap A[j] and A[j - 1]
        j ← j - 1
    end while
    i ← i + 1
end while
```

​    

- 삽입 정렬을 배열로 구현하면 제자리 정렬이 가능하여 공간 복잡도가 줄어든다.
  - 연결리스트로 구현할 때는 정렬된 리스트 변수를 별도 선언했음

```python
# Runtime 104 ms / Memory 14.3 MB
class Solution:
    
    # 문제에 적합한 비교 함수
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)
        
    # 삽입 정렬
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1
        
        return str(int(''.join(map(str, nums))))
```

  

- 입력 값이 ["0", "0"] 인 경우
  - 그냥 문자열로 처리하면 "00"이 되어버림
  - `join()` 결과를 `int`로 바꿔서 00이 0이 되도록 만들어 준 후, 다시 `str`로 변경

```python
return str(int(''.join(map(str, nums))))
```

  

### 내 풀이

```python
# Runtime 72 ms / Memory 14 MB
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(1, len(nums)):
            key = nums[i];
            j = i - 1;
            while j >= 0 and str(nums[j]) + str(key) < str(key) + str(nums[j]): 
                nums[j + 1] = nums[j];
                j = j - 1
            nums[j + 1] = key;
            
        return str(int(''.join(map(str, nums))))
```

