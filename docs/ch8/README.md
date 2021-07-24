# 8장 연결 리스트
## <a name='TOC'>목차</a>
0. [목차](#TOC)
1. [팰린드롬 연결 리스트(Palindrome Linked List)](#Palindrome)
2. [두 정렬 리스트의 병합(Merge Two Sorted Lists)](#mtsl)

## <a name='Palindrome'>#234 - 팰린드롬 연결 리스트(Palindrome Linked List)</a> 
### (1) 내 풀이
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getNext(self, head, total_list):
        if (head is not None):
            total_list.append(head.val)
            self.getNext(head.next, total_list)
        return total_list
    
    def checkEvenList(self, total_list):
        symmetric_ind = 0  # 대칭이 시작되는 ind - 1
        for i in range(0, len(total_list)-1):
            if total_list[i] == total_list[i+1]:
                symmetric_ind = i
        if (len(total_list) == (symmetric_ind+1)*2):
            distance = 1
            for i in range(symmetric_ind, -1, -1):
                if total_list[i] == total_list[symmetric_ind + distance]:
                    distance += 1
                    continue
                else:
                    return False
            return True
        else:
            return False
        
    def checkOddList(self, total_list):
        median_ind = len(total_list)//2
        distance = 1
        for i in range(median_ind, -1, -1):
            if total_list[median_ind - distance] == total_list[median_ind + distance]:
                distance += 1
                if (median_ind - distance) <= -1 :
                    return True
                else:
                    continue
            else:
                return False
        return False
    
    def isPalindrome(self, head: ListNode) -> bool:
        total_list = []
        total_list = self.getNext(head, total_list)
             
        if (len(total_list) == 0 or len(total_list) == 1):
            return True
        else:
            if (len(total_list) % 2 == 0):
                return self.checkEvenList(total_list)
            else:
                return self.checkOddList(total_list)
```
- 생각의 흐름
  - ListNode를 익숙한 list 자료형으로 바꾼다
  - 노드의 개수가 짝수인지 홀수인지에 따라 대칭점을 찾아서 대칭점을 기준으로 좌우의 값이 같은지 비교하고, 하나라도 다르면 False를 리턴한다.
- 평가
  - Runtime: 80 ms, faster than 22.68% of Python3 online submissions for Palindrome Linked List.
  - Memory Usage: 67.1 MB, less than 5.03% of Python3 online submissions for Palindrome Linked List.
  - 단순한 로직을 너무 조잡하게 구현했다. (고급화 필요)

### (2) 리스트 변환
```python3
def isPalindrome(self, head: ListNode) -> bool:
    q: List = []
        
    if not head:
        # 텅 비어 있는 ListNode라면 True 반환
        return True
    
    node = head
    # ListNode를 리스트로 변환
    while node is not None:
        q.append(node.val)
        node = node.next
    
    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            # 리스트 양단의 값이 동일하지 않으면 바로 False를 리턴
            return False
        
    return True
```
- list 자료형과 pop()을 이용함
  - list.pop() : list의 마지막 요소를 반환함과 동시에 제거해버림
  - list.pop(0) : list의 첫번째 요소를 반환함과 동시에 제거해버림

### (3) 데크를 이용한 최적화
```python3
def isPalindrome(self, head: ListNode) -> bool:
    # 데크 자료형 선언
    
    q: Deque = collections.deque()
    
    if not head:
        return True
    
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
    
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    
    return True
```
  - Collections 모듈의 deque를 활용함
  - [deque](https://excelsior-cjh.tistory.com/96)
    - Double Ended Queue / 스택, 큐, 연결리스트처럼 사용 가능
    - list 자료형과 다르게, 맨 앞의 데이터를 가져올 때 시간 복잡도 O(1)에 실행되어 더 효율적임
    - deque.pop() : 오른쪽(뒤)의 요소를 반환함과 동시에 제거
    - deque.popleft() : 왼쪽(앞)의 요소를 반환함과 동시에 제거

### (4) 고(Go)를 이용한 데크 구현
- 코드가 상당히 길지만, 속도가 Python3 보다 5배 정도 더 빠르다는 장점이 있음
- 파이썬 알고리즘 스터디이므로 패스.

### (5) 런너(Runner)를 이용한 우아한 풀이
```python3
def isPalindrome(self, head: ListNode) -> bool:
    # 예시1 : [3, 2, 1, 0, 1, 2, 3]
    # 예시2 : [2, 1, 1, 2]
    rev = None  # 추후 slow와의 비교를 위한, 중간 대칭점 이전까지의 역순 연결 리스트
    slow = fast = head  # 출발점을 잡음
    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next  # fast는 두 칸씩 달려감
        rev, rev.next, slow = slow, rev, slow.next  # rev는 앞에 계속 새 노드가 추가되고, slow는 한 칸씩 달려감
    if fast:
        # 노드의 수가 홀수일 때, slow를 한 칸 더 이동해서 중앙의 대칭점을 벗어나도록 한다.
        slow = slow.next
        
    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev
```
- ListNode를 있는 그대로 이용하는 방법 (다른 풀이 대비 list로 변환하는 시간을 없앰)
  - ![KakaoTalk_20210117_105548836](https://user-images.githubusercontent.com/75566147/104829015-d2439700-58b2-11eb-8664-f95d98bbf499.jpg)
  - ![KakaoTalk_20210117_105606655](https://user-images.githubusercontent.com/75566147/104829016-d40d5a80-58b2-11eb-9ac8-bdc1a0a4e257.jpg)
- [런너(Runner)](https://www.pluralsight.com/guides/algorithm-templates:-two-pointers-part-1)
  - 연결 리스트 순회 시 2개의 포인터를 동시에 사용하여, 병합 지점/중간점/길이 등을 판별할 때 유용함
- 다중 할당(Multiple Assignments)
  - 쓰면 유용할 때가 있고, 써서는 안 될 때가 있음
  - "Python 에서는 모든 것이 객체이기 때문에, '='은 값 할당이 아니라 같은 값을 참조하는 것이다"



## <a name='mtsl'>#21 - 두 정렬 리스트의 병합(Merge Two Sorted Lists)</a> 
### (1) 내 풀이
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listToListnode(self, result):
        if not result:
            return ListNode('')
        else:
            ind = 1
            start = ListNode(result[0])
            end = start
            while ind < len(result):
                end.next= ListNode(result[ind])
                end = end.next
                ind += 1
            return start
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged_list = []
        while l1 and l2:
            if l1.val < l2.val:
                merged_list.append(l1.val)
                l1 = l1.next
            else:
                merged_list.append(l2.val)
                l2 = l2.next
        if l1:
            while l1:
                merged_list.append(l1.val)
                l1 = l1.next
        if l2:
            while l2:
                merged_list.append(l2.val)
                l2 = l2.next
        return self.listToListnode(merged_list)
```
- 생각의 흐름
  - 두 list의 각 원소를 대소(大小)비교 하여, 값이 더 작은 원소부터 먼저 결과 list에 추가함
  - 결과 list를 ListNode 형태로 변환한 후 리턴
- 평가
  - Runtime: 36 ms, faster than 75.05% of Python3 online submissions for Merge Two Sorted Lists.
  - Memory Usage: 14.2 MB, less than 83.79% of Python3 online submissions for Merge Two Sorted Lists.
  - 앞서 234 팰린드롬 문제보다는 런타임이 낫지만, 여전히 코드가 조잡한 느낌이 있다.

### (2) 재귀 구조로 연결
```python3
def mergeTowLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1
```
- 이해
  - ![KakaoTalk_20210117_105630099](https://user-images.githubusercontent.com/75566147/104829199-d40e5a00-58b4-11eb-9c26-568950a17f68.jpg)
- [연산자 우선순위](https://wikidocs.net/20708)
  - 이 문제에서 나온 연산자만 따지면 : 괄호 - > - 논리not - 논리and - 논리or 
- 변수 스왑 방법 (둘 간의 속도의 차이는 크게 없음)
  - 임시 변수 사용
  - 다중 할당 사용 : "more pythonic way!"
