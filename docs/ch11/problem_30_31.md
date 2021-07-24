## 30. 중복 문자 없는 가장 긴 부분 문자열

- https://leetcode.com/problems/longest-substring-without-repeating-characters/

>**3. Longest Substring Without Repeating Characters** (Medium)
>
>Given a string `s`, find the length of the **longest substring** without repeating characters.
>
>**Example 1:**
>
>```
>Input: s = "abcabcbb"
>Output: 3
>Explanation: The answer is "abc", with the length of 3.
>```
>
>**Example 2:**
>
>```
>Input: s = "bbbbb"
>Output: 1
>Explanation: The answer is "b", with the length of 1.
>```
>
>**Example 3:**
>
>```
>Input: s = "pwwkew"
>Output: 3
>Explanation: The answer is "wke", with the length of 3.
>Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
>```
>
>**Example 4:**
>
>```
>Input: s = ""
>Output: 0
>```
>
>**Constraints:**
>
>- `0 <= s.length <= 5 * 104`
>- `s` consists of English letters, digits, symbols and spaces.

### 1) 슬라이딩 윈도우와 투 포인터로 사이즈 조절

- 입력값이 `s = "abcabcbb"`인 경우
- 슬라이딩 윈도우를 한 칸씩 우측으로 이동하면서 윈도우 내에 모든 문자가 중복이 없도록 투 포인터로 윈도우 사이즈 조절

![image](https://user-images.githubusercontent.com/19264527/108612199-a2dff700-7429-11eb-996a-99285dec52b0.png)

#### 코드 구현

- 투 포인터로 문제 풀이

- 포인터 2개 모두 왼쪽에서 출발

- 우측 포인터(`index`)는 오른쪽으로 계속 확장

- 이미 등장한 문자라면 좌측 포인터(`start`)를 `used[char] + 1` 위치로 갱신

  ```python
  for index, char in enumerate(s):
      if char in used:
          start = used[char] + 1
      else: 
          ...
  ```

- 처음보는 문자인 경우, 매번 `max()`로 부분 문자열의 길이를 확인하면서 더 큰값인 경우 갱신

  ```python
  for index, char in enumerate(s):
      if char in used:
          ...
      else: 
        	max_length = max(max_length, index - start + 1)
  ```

- `used[char]` - 현재 문자를 키로 하는 해시 테이블 (현재 위치 삽입)

- 이미 등장했다고 무작정 `start`를 옮겨버리지 않고, 슬라이딩 윈도의 바깥에 있는 문자는 예전에 등장한 적 있더라도 무시

  ```python
  for index, char in enumerate(s):
      if char in used and start <= used[char]:
          ...
      else: 
          ...
  ```

#### 전체 풀이

```python
# Runtime 48 ms / Memory 14.3 MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 'start' 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else: # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)
            
            # 현재 문자의 위치 삽입
            used[char] = index
        
        return max_length
```

   

## 31. 상위 K 빈도 요소

- https://leetcode.com/problems/top-k-frequent-elements/

>**347. Top K Frequent Elements** (Medium)
>
>Given a non-empty array of integers, return the ***k\*** most frequent elements.
>
>**Example 1:**
>
>```
>Input: nums = [1,1,1,2,2,3], k = 2
>Output: [1,2]
>```
>
>**Example 2:**
>
>```
>Input: nums = [1], k = 1
>Output: [1]
>```
>
>**Note:**
>
>- You may assume *k* is always valid, 1 ≤ *k* ≤ number of unique elements.
>- Your algorithm's time complexity **must be** better than O(*n* log *n*), where *n* is the array's size.
>- It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
>- You can return the answer in any order.

### 1)  Counter를 이용한 음수 순 추출

- 빈도수는 `collections.Counter` 사용하여 쉽게 구현

  ```python
  freqs = collections.Counter(nums)
  
  >>> type(s.freqs)
  collections.Counter
  >>> s.freqs
  Counter({
    1: 3,
    2: 2,
    3: 1
  })
  ```

- 힙에 삽입

  1. 파이썬의 리스트에 모두 삽입한 다음 마지막에 `heapify()`
  2. 매번 `heappush()`를 하는 방식 (내부적으로 매번 `heapify()` 동작)

  ```python
  # 힙에 음수로 삽입 (heapq 모듈은 최소 힙만 지원하기 때문)
  for f in freqs:
      heapq.heappush(freqs_heap, (-freqs[f], f))
  ```

- `heappop()`으로 k번만큼 값을 추출

  ```python
  topk = list()
  # k번 만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출
      topk.append(heapq.heappop(freqs_heap)[1])
  ```

#### 전체 풀이

```python
# Runtime 100 ms / Memory 18.8 MB
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
            
        topk = list()
        # k번 만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
            
        return topk
```

### 2) 파이썬다운 방식

- `Counter`의 `most_common()` - 빈도 수가 높은 순서대로 아이템을 추출

  ```python
  >>> collections.Counter(nums).most_common(k)
  [(1, 3), (2, 2)]
  ```

- 정답 추출을 위해 파이썬의 `zip()`, `*`(별표) 를 사용

```python
# Runtime 104 ms / Memory 18.5 MB
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
```

### 풀이 비교

| 풀이 | 방식                          | 실행시간 |
| ---- | ----------------------------- | -------- |
| 1    | Counter를 이용한 음수 순 출력 | 108 ms   |
| 2    | 파이썬다운 방식               | 104 ms   |

## 문법 - zip() 함수

- 2개 이상의 시퀀스를 짧은 길이를 기준으로 일대일 대응하는 새로운 튜플 시퀀스를 만드는 역할

  - Python2 - 바로 리스트 리턴
  - Python3 - 제너레이터 리턴

  ```python
  >>> a = [1, 2, 3, 4, 5]
  >>> b = [2, 3, 4, 5]
  >>> c = [3, 4, 5]
  >>> zip(a, b)
  <zip object at 0x105b6d9b0>
  ```

- 제너레이터에서 실제값을 추출하기 위해서 `list()`로 한번 더 묶어 준다

  ```python
  >>> list(zip(a, b))
  [(1, 2), (2, 3), (3, 4), (4, 5)]
  >>> list(zip(a, b, c))
  [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
  ```

- `zip()`의 결과 자체는 리스트 시퀀스가 아닌 튜플 시퀀스 (값 변경 불가능한 불변 객체)

  ```python
  >>> d = list(zip(a, b, c))
  >>> d[0]
  (1, 2, 3)
  >>> d[0][0]
  1
  >>> d[0][0] = 0
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: 'tuple' object does not support item assignment
  ```

## 문법 - 아스테리스크(*)

- `zip()`의 파라미터는 1개가 될 수도 10개가 될 수도 있다.

- 아스테리스크(Asterisk) 혹은 별표라고 부르는 `*`를 활용

- 시퀀스 언패킹 연산자(Sequence Unpacking Operator) -  시퀀스를 풀어헤치는 연산자 (주로 튜플이나 리스트를 언패킹하는데 사용)

  ```python
  >>> collections.Counter(nums).most_common(k)
  [(1, 3), (2, 2)]
  # 언패킹을 했을 때
  >>> list(zip(*collections.Counter(nums).most_common(k)))
  [(1, 2), (3, 2)]
  # 언패킹을 하지 않았을 때
  >>> list(zip(collections.Counter(nums).most_common(k)))
  [((1, 3),), ((2, 2),)]
  
  >>> fruits = ['lemon', 'pear', 'watermelon', 'tomato']
  >>> print(*fruits)
  lemon pear watermelon tomato
  ```

- 함수의 파라미터가 되었을 때는 반대로 패킹(Packing) 

  - `zip()`에 파라미터를 여러개 쓸 수 있는 것도 내부적으로 *로 패킹하고 있는 것
  - `print()` 함수의 기본 동작 원리

  ```python
  >>> def f(*params):
  ... 	print(params)
  ...
  >>> f('a', 'b', 'c')
  ('a', 'b', 'c')
  ```

- `**` - 키/값 페어를 언패킹 (`*` - 튜플 또는 시퀀스 언패킹)

  ```python
  >>> date_info = {'year': '2020', 'month': '01', 'day': '7'}
  >>> new_info = {**date_info, 'day' : "14"}
  >>> new_info
  {'year': '2020', 'month': '01', 'day': '14'}
  ```

  

