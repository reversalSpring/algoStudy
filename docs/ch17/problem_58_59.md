# 17장 정렬
## <a name='TOC'>목차</a>
0. [목차](#TOC)
1. [정렬](#0)
2. [리스트 정렬(Sort List)](#1)
3. [구간 병합(Merge Intervals)](#2)

## <a name='0'>정렬</a>
### (1) [Bubble Sort](https://gmlwjd9405.github.io/2018/05/06/algorithm-bubble-sort.html)
![image](https://user-images.githubusercontent.com/75566147/114269803-c98ed700-9a43-11eb-8d06-925493e96e5e.png)
### (2) [Merge Sort](https://gmlwjd9405.github.io/2018/05/08/algorithm-merge-sort.html)
![image](https://user-images.githubusercontent.com/75566147/114255129-6757b700-99ee-11eb-87e6-3ae62dec71f1.png)
### (3) [Quick Sort](https://gmlwjd9405.github.io/2018/05/10/algorithm-quick-sort.html)
![image](https://user-images.githubusercontent.com/75566147/114269843-08249180-9a44-11eb-9f02-bc94839779e8.png)
![image](https://user-images.githubusercontent.com/75566147/114269910-63ef1a80-9a44-11eb-9118-e5055cc14ca9.png)
### (4) Stable Sort VS Unstable Sort
- "정렬되지 않은 상태에서 같은 키값을 가진 원소의 순서가 정렬 후에도 유지되느냐"
- 더 자세한 설명은 [링크 클릭](https://godgod732.tistory.com/10)

### (5) [정렬 알고리즘 비교](https://titrias.com/ultimate-sorting-algorithms-comparison/)
||버블(Bubble)|병합(Merge)|퀵(Quick)|
|---|---|---|---|
|Average|О(n^2)|O(nlog(n))|O(nlog(n))|
|Worst|О(n^2)|O(nlog(n))|О(n^2)|
|Best|О(n)|O(nlog(n))|O(nlog(n))|
|분류|Unstable|Stable|Unstable|

![image](https://user-images.githubusercontent.com/75566147/114269536-ad3e6a80-9a42-11eb-945c-b0bcf7d7a663.png)


## <a name='1'>[#148 - 리스트 정렬(Sort List)](https://leetcode.com/problems/sort-list/)</a>
### 문제
![image](https://user-images.githubusercontent.com/75566147/114254769-41c9ae00-99ec-11eb-8fbc-2644e24faa8a.png)
### (1) 내 풀이
```python3
class Solution:
    def linkedToSimple(self, linkedList):
        result = []
        while(linkedList is not None):
            result.append(linkedList.val)
            linkedList = linkedList.next
        return result
    
    
    def simpleToLinked(self, arr):
        cur = dummy = ListNode(0)
        for e in arr:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next            
    
    
    def mergeSort(self, arr):
        if len(arr) > 1:
            med = len(arr)//2
            L = arr[:med]
            R = arr[med:]
            
            self.mergeSort(L)
            self.mergeSort(R)
            
            i = j = k = 0
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
 
            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
 
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr
    
    
    def sortList(self, head: ListNode) -> ListNode:
        targetList = self.linkedToSimple(head)
        if len(targetList) <= 1:
            return head
        result = self.simpleToLinked(self.mergeSort(targetList))
        return result
```
- Point
  - O(nlogn)을 원했으니 Merge Sort를 사용
  - 주어진 ListNode를 그대로 사용하지 않고, list로 변환해서 merge sort를 적용한 다음 다시 ListNode 형태로 

### (2) 책 풀이 - 병합 정렬(Merge Sort)
```python3
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
        
        
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
    
        # 런너 기법 활용
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None
    
        # 분할 재귀 호출
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
    
        return self.mergeTwoLists(l1, l2)
```
- Point
  - ListNode 형태 그대로 풀어냄 (굳이 list로 변환하지 않음)
  - //2 대신 런너 기법을 사용해서 중앙값을 찾음 (본문 p210 참고)
  - ![image](https://user-images.githubusercontent.com/75566147/114269365-a06d4700-9a41-11eb-9ced-d63ea79d2493.png)

### (3) 책 풀이 - 내장 함수를 이용하는 실용적인 방법
```python3
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 연결 리스트 -> 파이썬 리스트
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next
    
        # 정렬
        lst.sort()
        
        # 파이썬 리스트 -> 연결 리스트
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head
```
- Point
  - ListNode를 list로 변환함
  - 정렬을 위해 내장함수 sort()를 사용
  - 다시 list를 ListNode 형태로 변환함
  - p는 ListNode를 순회하기 위한 포인터 변수

### (4) 비교분석
![image](https://user-images.githubusercontent.com/75566147/114269151-22f50700-9a40-11eb-89cc-f899e3b32e41.png)

  

## <a name='2'>[#56 - 구간 병합(Merge Intervals)](https://leetcode.com/problems/merge-intervals/)</a>
### 문제
![image](https://user-images.githubusercontent.com/75566147/114270011-04ddd580-9a45-11eb-957c-1e16de135867.png)
### (1) 내 풀이 - 전부 실패..
```python3
# 실패 1
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        simpleList = list()
        featureMap = dict()
        for elem in intervals:
            simpleList.append(elem[0])
            simpleList.append(elem[1])
            featureMap[elem[0]] = 'S'
            featureMap[elem[1]] = 'E'
        simpleList.sort()
        
        result = list()
        mini = list()
        for i in range(len(simpleList)):
            if i == 0:
                mini.append(simpleList[i])
                continue
            if i == len(simpleList)-1:
                mini.append(simpleList[i])
                result.append(mini)
                break
            if featureMap[simpleList[i]] == 'S' and featureMap[simpleList[i-1]] != 'S':
                mini.append(simpleList[i])
            elif featureMap[simpleList[i]] == 'E' and featureMap[simpleList[i+1]] == 'S':
                mini.append(simpleList[i])
            i += 1
            if len(mini) == 2:
                result.append(mini)
                mini = list()
        return result
```
```python3
# 실패 2
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        simpleList = list()
        featureMap = dict()
        for elem in intervals:
            simpleList.append(elem[0])
            simpleList.append(elem[1])
            featureMap[elem[0]] = 'S'
            featureMap[elem[1]] = 'E'
        simpleList.sort()
        
        result = list()
        mini = list()
        for i in range(len(simpleList)):
            curr = simpleList[i]
            if i == 0:
                mini.append(curr)
                continue
            prev = simpleList[i-1]
            
            if i == len(simpleList)-1:
                mini.append(curr)
                result.append(mini)
                break
            next = simpleList[i+1]
            
            if featureMap[curr] == 'S':
                if featureMap[prev] == 'E' and i%2 == 0:
                    mini.append(curr)
            else:
                if featureMap[next] == 'S' and i%2 != 0:
                    mini.append(curr)
            i += 1
            
            if len(mini) == 2:
                result.append(mini)
                mini = list()
        return result
```
```python3
# 실패 3
class Solution:
    def getMapList(self, featureMap, arr):
        result = list()
        for elem in arr:
            result.append(featureMap[elem])
        return result
    
        
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        simpleList = list()
        featureMap = dict()
        for elem in intervals:
            simpleList.append(elem[0])
            simpleList.append(elem[1])
            featureMap[elem[0]] = 'S'
            featureMap[elem[1]] = 'E'
        simpleList.sort()
        
        letterList = self.getMapList(featureMap, simpleList)
        prev_c = collections.Counter(letterList)
        if prev_c.most_common(1)[0][1] == len(letterList):
            return intervals
        
        result = list()
        mini = list()
        mini_start = 0
        mini_last_val = 0
        for i in range(len(letterList)):
            if i == 0:
                mini.append(simpleList[0])
                continue
            if i == len(letterList)-1:
                mini.append(simpleList[i])
                result.append(mini)
                break
            # S~E 혹은 E~E 사이에 (a) SE가 같은수만큼 있거나 (b) S 또는 E 한종류만 차 있거나
            if len(mini) == 0:
                if mini_last_val != simpleList[i]:
                    mini.append(simpleList[i])
                    mini_start = i
            else:
                # 이미 mini에 뭔가 하나 들어 있는 경우
                if (letterList[mini_start] == 'S' and letterList[i] == 'E') or (letterList[mini_start] == 'E' and letterList[i] == 'E'):
                    c = collections.Counter(letterList[mini_start:i])
                    if letterList[mini_start] == 'S':
                        if (c['S']-1 == c['E']) or (c['S'] != 1 and c['E'] == 0) or (c['S'] == 1 and c['E'] != 0):
                            if (letterList[i+1] != 'E'):
                                mini.append(simpleList[i])
                                mini_last_val = simpleList[i]
                    else:
                        if (c['S'] == c['E']-1) or (c['S'] != 0 and c['E'] == 1) or (c['S'] == 0 and c['E'] != 1):
                            mini.append(simpleList[i])
                            mini_last_val = simpleList[i]
                    
            i += 1
            if len(mini) == 2:
                result.append(mini)
                mini = list()
        return result
```
- 망한 Point
  - 주어진 intervals의 원소마다, 앞에 있는 것은 'S'/ 뒤에 있는 것은 'E'라는 값을 부여해서 dict로 저장하고
  - SSESEE / EEESSSEEEE / SSEESESE 등 나오는 문자열에서 어떤 패턴을 찾아서 이를 기반으로 구간 병합을 하고자 했으나 FAIL

### (2) 책 풀이 - 정렬하여 병합 ([유사 풀이](https://leetcode.com/problems/merge-intervals/discuss/350272/Python3-Sort-O(Nlog(N))))
```python3
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,  # merged.append(i)
        return merged
```
![image](https://user-images.githubusercontent.com/75566147/114277074-99a3fb80-9a64-11eb-9044-a1623f561b8b.png)
- Point
  - 주어진 intervals의 각 요소마다, 앞에 있는 값을 기준으로 정렬
  - 정렬된 것을 돌면서 i+1 번째의 구간의 i번째의 구간과 겹치면 업데이트 하고
  - 그렇지 않으면 새로 추가한다

### (3) 동일한 테크닉으로 풀 수 있는 다른 문제들 ([출처](https://leetcode.com/problems/merge-intervals/discuss/21227/7-lines-easy-Python)의 첫번째 댓글)
- 링크
  - https://leetcode.com/problems/meeting-rooms/
  - https://leetcode.com/problems/meeting-rooms-ii/
  - https://leetcode.com/problems/non-overlapping-intervals/

