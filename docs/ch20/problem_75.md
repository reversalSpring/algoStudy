# 20장 슬라이딩 윈도우
## <a name='TOC'>목차</a>
0. [목차](#TOC)
1. [슬라이딩 윈도우 알고리즘](#1)
2. [최대 슬라이딩 윈도우 (Sliding Window Maximum)](#2)

## <a name='1'>[이론] 슬라이딩 윈도우 알고리즘</a>
![image](https://miro.medium.com/max/1912/1*HN084lMD15SWjH6epVeSAg.gif)

### 특징
||투 포인터|슬라이딩 윈도우|
|---:|---|---|
|쓰임새|특정 조건을 만족하는 "연속 구간"을 구할 때 O(N) 으로 풀 수 있도록 도와주는 알고리즘||
|구간|가변적인 크기로 구간을 움직임(포인터 두 개 필요)|고정적인 크기로 구간을 움직임(포인터가 하나면 됨)|
|포인터|서로 독립적으로 움직임|같이 움직임|
|구현|[참고](https://www.pluralsight.com/guides/algorithm-templates:-two-pointers-part-1)|주로 deque 사용|

- 주로 [deque](https://chaewonkong.github.io/posts/python-deque.html)를 이용하여 풀이
  - ```python3
    from collections import deque
    
    deq = deque()
    
    # Add element to the start
    deq.appendleft(10)
    
    # Add element to the end
    deq.append(0)
    
    # Pop element from the start
    deq.popleft()
    
    # Pop element from the end
    deq.pop()
    ```
- string, array, linked list 처럼 연속적인 타입에 활용 가능
- 문제 예시 : Minimum / Maximum / Longest / Shortest / K-sized value 등을 구하라고 할 때
- 참고
  - https://levelup.gitconnected.com/an-introduction-to-sliding-window-algorithms-5533c4fe1cc7
  - https://code0xff.tistory.com/168?category=723754
  - [적용 가능한 문제 모음 1](https://m.blog.naver.com/kks227/220795165570)
  - [적용 가능한 문제 모음 2](https://ansohxxn.github.io/algorithm/twopointer/)

## <a name='2'>[#239 - 최대 슬라이딩 윈도우 (Sliding Window Maximum)](https://leetcode.com/problems/sliding-window-maximum/)</a>
### 문제
![image](https://user-images.githubusercontent.com/75566147/118351764-b7e7a480-b598-11eb-9225-916f51de225a.png)

### (1) 내 풀이 - Time Limit Exceeded
```python3
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_vals = []
        
        for i in range(len(nums)):
            if i+k <= len(nums):
                max_vals.append(max(nums[i:i+k]))
        
        return max_vals
```
- Point
  - 단순하게 생각하고 푼 결과 최적화에 실패하여 타임아웃이 남

### (2) 내 풀이 - 최적화
```python3
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        result = []
        
        for i,v in enumerate(nums):           
            while dq and dq[-1][1] < v:
                # v 보다 작은 값은 다 버린다.
                dq.pop()
            
            dq.append((i, v))  # deque에 튜플 형태로 저장한다: (index, value)
            
            while dq and dq[0][0] < i - k + 1:
                # 윈도우 범위를 벗어나면 버린다
                dq.popleft()
            
            result.append(dq[0][1])
        
        return result[k-1:]
```
- Point
  - deque를 사용
  - https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/

### (3) 책 풀이 - 브루트 포스로 계산 -> leetcode에서는 마찬가지로 Time Limit Exceeded
```python3
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums
        
        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i+k]))
        
        return r
```
- Point
  - k 크기의 윈도우를 1씩 오른쪽으로 이동하며 max()로 매번 최댓값을 추출

### (4) 책 풀이 - 큐를 이용한 최적화
```python3
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k-1:
                continue
            
            # 새로 추가한 값이 기존 최댓값보다 큰 경우 교체
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v
            
            results.append(current_max)
            
            # 최댓값이 윈도우에서 빠지면 초기화
            if current_max == window.popleft():
                current_max = float('-inf')
                
       return results
```
- Point
  - 최댓값 계산을 최소화 함
  - 이전 범위에서의 최댓값을 저장해두고, 이를 새로 윈도우 범위에 들어 온 값과 비교한다. 
  - 단, 이전 최댓값이 윈도우 범위에서 빠지게 된다면 그 때만 윈도우 전체 범위 내에서 max를 새로 뽑아낸다.

### (4) 성능 비교
||방식|실행 시간(ms)|
|---|---|---|
|나|단순 반복 & max() 찾기|Timeout|
|나|deque를 이용한 최적화|1792|
|책|브루트 포스로 계산|Timeout|
|책|큐를 이용한 최적화|156|

끝.

