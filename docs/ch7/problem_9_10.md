# 7장 배열

## 9. 세 수의 합

- https://leetcode.com/problems/3sum

>**15. 3Sum** (Medium)
>
>Given an array `nums` of *n* integers, are there elements *a*, *b*, *c* in `nums` such that *a* + *b* + *c* = 0? Find all unique triplets in the array which gives the sum of zero.
>
>Notice that the solution set must not contain duplicate triplets.
>
>**Example 1:**
>
>```
>Input: nums = [-1,0,1,2,-1,-4]
>Output: [[-1,-1,2],[-1,0,1]]
>```
>
>**Example 2:**
>
>```
>Input: nums = []
>Output: []
>```
>
>**Example 3:**
>
>```
>Input: nums = [0]
>Output: []
>```
>
>**Constraints:**
>
>- `0 <= nums.length <= 3000`
>- `-105 <= nums[i] <= 105`

  

### 1) 브루트 포스로 계산

1. 앞 뒤로 같은 값이 있는 경우 처리 용이를 위해`sort()` 함수로 정렬 - <img src="https://latex.codecogs.com/gif.latex?O(nlogn)" />

2. `i`, `j`, `k`  세 포인터가 계속 이동하면서 `i + j + k = 0`을 찾아낸다.

3. 중복 처리

   ```python
   if i > 0 and nums[i] == nums[i - 1]:
     continue
   ```

- 시간복잡도가 <img src="https://latex.codecogs.com/gif.latex?O(n^3)" /> 으로 타임 아웃. <img src="https://latex.codecogs.com/gif.latex?O(n^2)" /> 으로 최적화 필요

```python
# Time Limit Exceeded
def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    # 브루트 포스 n^3 반복
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append((nums[i], nums[j], nums[k]))

    return result
```

  

### 2) 투 포인터로 합 계산

1. `sort()` 함수로 정렬 - <img src="https://latex.codecogs.com/gif.latex?O(nlogn)" />
2. `i`를 축으로 하고, 중복 처리
3. 투 포인터 `left`, `right`로 간격을 좁혀가며 `i`와의 합 계산
4. `sum`과 0의 값 비교
   - `sum < 0` - 값을 키워야 하므로 `left` 우측 이동
   - `sum > 0` - 값을 줄여야 하므로 `right` 좌측 이동
   - `sum == 0` - 정답, 결과를 리스트에 추가
     - 양 옆에 동일한 값이 있을 수도 있으므로 반복해서 스킵 처리
     - `left`를 한 칸 우측, `right`를 한 칸 좌측 이동 (어짜피 sum=0이므로 중복된 값 필요 없음)

```python
# Runtime 1016 ms / Memory 17 MB
def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격을 좁혀 합 sum 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0인 경우이므로 정답 및 스킵 처리
                result.append((nums[i], nums[left], nums[right]))

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result
```

- 살짝 다른 풀이 (정답 찾은 후에는 `right`를 이동하지 않음)

```python
# Runtime 812 ms / Memory 17 MB
def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res
```

  

### 풀이 비교

| 풀이 | 방식                | 실행시간 |
| ---- | ------------------- | -------- |
| 1    | 브루트 포스로 계산  | 타임아웃 |
| 2    | 투 포인터로 합 계산 | 884 ms   |

  

###  투 포인터(Two Pointers)

- 시작점과 끝점 / 왼쪽 포인터와 오른쪽 포인터 두 지점을 기준으로 하는 문제 풀이 전략
- 범위를 좁혀 나가기 위해서는, 일반적으로 정렬된 배열이 유용
- 실전적인 풀이 기법
- 슬라이딩 윈도우(Sliding Window, 20장)와 비슷한 점이 많음. 

   

## 10. 배열 파티션 1

- https://leetcode.com/problems/array-partition-i/

>**561. Array Partition I** (Easy)
>
>Given an integer array `nums` of `2n` integers, group these integers into `n` pairs `(a1, b1), (a2, b2), ..., (an, bn)` such that the sum of `min(ai, bi)` for all `i` is **maximized**. Return *the maximized sum*.
>
>**Example 1:**
>
>```
>Input: nums = [1,4,3,2]
>Output: 4
>Explanation: All possible pairings (ignoring the ordering of elements) are:
>1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
>2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
>3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
>So the maximum possible sum is 4.
>```
>
>**Example 2:**
>
>```
>Input: nums = [6,2,6,5,1,2]
>Output: 9
>Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
>```
>
>**Constraints:**
>
>- `1 <= n <= 104`
>- `nums.length == 2 * n`
>- `-104 <= nums[i] <= 104`

- 페어의 `min()`을 합산했을 때 최대를 만드는 문제

  

### 내 풀이

```python
# Runtime 388 ms / Memory 16.9 MB
def arrayPairSum(self, nums: List[int]) -> int:
    nums.sort()
    sum = 0
    for i in range(0, len(nums), 2):
        sum += nums[i]
    return sum
```

  

### 1) 오름 차순 풀이

- 뒤에서부터 내림차순으로 집어 넣으면 항상 최대 `min()` 페어를 유지할 수 있다
- 배열 입력값은 항상 <img src="https://latex.codecogs.com/gif.latex?2n" /> 개일 것이므로 앞에서부터 오름차순으로 집어넣어도 결과는 같다.
- 예시) 1, 2, 3, 4 로 만든 3가지 조합
  1. min(1, 4) + min(2, 3) = 3
  2. min(1, 3) + min(2, 4) = 3
  3. min(1, 2) + min(3, 4) = 4 

```python
# Runtime 440 ms / Memory 16.7 MB
def arrayPairSum(self, nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()
    
    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
            
    return sum
```

  

 ### 2) 짝수 번째 값 계산

- 페어에 대해 일일이 `min()` 값을 구하지 않아도 짝수 번째 값을 더하면 된다.
- 정렬된 상태에서 짝수 번째에 항상 작은 값이 위치하기 때문.

```python
# Runtime 308 ms / Memory 17 MB
def arrayPairSum(self, nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째 값의 합 계산
        if i % 2 == 0:
            sum += n

    return sum
```

  

### 3) 파이썬다운(Pythonic Way) 방식

- 슬라이싱 활용하여 성능 향상 및 한 줄 풀이 

  ```python
    # Runtime 264 ms / Memory 16.8 MB
    def arrayPairSum(self, nums: List[int]) -> int:
    return sum(sorted(nums)[::2])
  ```

- `sorted`(*iterable*, *, *key=None*, *reverse=False*)[¶](https://docs.python.org/3/library/functions.html#sorted)

  : Return a new sorted list from the items in *iterable*.

- `[::2]`- 2칸씩 건너뛰기

- `sum`(*iterable*, */*, *start=0*)[¶](https://docs.python.org/3/library/functions.html#sum)

  : Sums *start* and the items of an *iterable* from left to right and returns the total. 

  

### 풀이 비교

- 2번 풀이 - `min()`을 계산하지 않고 단순히 해당 인덱스를 찾으면 됨
- 3번 풀이 - 슬라이싱 사용하여 성능 가장 좋음

| 풀이 | 방식              | 실행시간 |
| ---- | ----------------- | -------- |
| 1    | 오름차순 풀이     | 332 ms   |
| 2    | 짝수 번째 값 계산 | 308 ms   |
| 3    | 파이썬다운 방식   | 284 ms   |

  