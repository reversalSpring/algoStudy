## 66. 회전 정렬된 배열 검색

- https://leetcode.com/problems/search-in-rotated-sorted-array/

>**33. Search in Rotated Sorted Array** (Medium)
>
>There is an integer array `nums` sorted in ascending order (with **distinct** values).
>
>Prior to being passed to your function, `nums` is **rotated** at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.
>
>Given the array `nums` **after** the rotation and an integer `target`, return *the index of* `target` *if it is in* `nums`*, or* `-1` *if it is not in* `nums`.
>
> 
>
>**Example 1:**
>
>```
>Input: nums = [4,5,6,7,0,1,2], target = 0
> Output: 4
>```
>
>**Example 2:**
>
>```
>Input: nums = [4,5,6,7,0,1,2], target = 3
>Output: -1
>```
>
>**Example 3:**
>
>```
>Input: nums = [1], target = 0
>Output: -1
>```
>
> 
>
>**Constraints:**
> 
>- `1 <= nums.length <= 5000`
>- `-104 <= nums[i] <= 104`
>- All values of `nums` are **unique**.
>- `nums` is guaranteed to be rotated at some pivot.
>- `-104 <= target <= 104`

  

### 1) 피벗을 기준으로 한 이진 검색

- 정렬이 되어 있긴 한데, 피벗을 기준으로 값이 돌아간 상황

1. 피벗 찾기

   - 최솟값의 인덱스가 피벗
   - 이진 검색으로 찾기

   ```python
   left, right = 0, len(nums) - 1
   while left < right:
       mid = left + (right - left) // 2
               
       if nums[mid] > nums[right]:
           left = mid + 1
       else:
           right = mid
   pivot = left
   ```

   - `NumPy` 모듈 활용

   ```python
   pivot = numpy.argmin()
   ```

   - 파이썬 다운 코드

   ```python
   pivot = nums.index(min(nums))
   ```

2. 피벗 기준 이진 검색으로 값의 인덱스 찾기

   - 최솟값 `left`를 피벗으로 구성
   - 피벗의 위치만큼 살짝 틀어준 `mid_pivot`을 구성
   - 이진 검색을 통해 `target` 값 찾기
   - 실제 값에 대한 비교는 `mid_pivot` 기준으로 함.

   ```python
   # 피벗 기준 이진 검색
   left, right = 0, len(nums) - 1
   while left <= right:
       mid = left + (right - left) // 2
       mid_pivot = (mid + pivot) % len(nums)
               
       if nums[mid_pivot] < target:
           left = mid + 1
       elif nums[mid_pivot] > target:
           right = mid - 1
       else:
           return mid_pivot
   ```

   ![image](https://user-images.githubusercontent.com/19264527/115975528-8898d580-a5a0-11eb-958f-53867c9771c1.png)

```python
# Runtime 36 ms / Memory 14.7 MB
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 예외 처리
        if not nums:
            return -1
        
        # 최솟값을 찾아 피벗 설정
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        pivot = left
        
        # 피벗 기준 이진 검색
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)
            
            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
                
        return -1
```

​          

## 67. 두 배열의 교집합

- https://leetcode.com/problems/intersection-of-two-arrays/

>**349. Intersection of Two Arrays** (Easy)
>
>Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must be **unique** and you may return the result in **any order**.
>
> 
>
>**Example 1:**
>
>```
>Input: nums1 = [1,2,2,1], nums2 = [2,2]
>Output: [2]
>```
>
>**Example 2:**
>
>```
>Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
>Output: [9,4]
>Explanation: [4,9] is also accepted.
>```
>
> 
>
>**Constraints:**
>
>- `1 <= nums1.length, nums2.length <= 1000`
>- `0 <= nums1[i], nums2[i] <= 1000`

  

### 1)  브루트 포스로 계산

- ![image](https://user-images.githubusercontent.com/19264527/115976170-1a571180-a5a6-11eb-875f-123882968ef8.png) 반복
- 데이터 타입이 집합(set)이므로 속도는 느리지만 중복 처리해줌.

```python
# Runtime 136 ms / Memory 14.5 MB
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    result.add(n1)
                    
        return result
```

​    

### 2) 이진 검색으로 일치 여부 판별

- 한 쪽은 순서대로 탐색하고 다른 쪽은 정렬해서 이진 검색으로 찾으면 검색 효율을 높일 수 있다. - ![image](https://user-images.githubusercontent.com/19264527/115976144-e7148280-a5a5-11eb-9954-1353a33cefd2.png)
- `nums2`는 정렬한 상태에서, `nums1`을 순차 반복하면서 `nums2`를 ![image](https://user-images.githubusercontent.com/19264527/115976190-5db18000-a5a6-11eb-9877-5fd6ffb1d261.png) 이진 검색

```python
# Runtime 40 ms / Memory 14.2 MB
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums2.sort()
        for n1 in nums1:
            # 이진 검색으로 일치 여부 판별
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)
                    
        return result
        
```

​    

### 3) 투 포인터로 일치 여부 판별

- 양쪽 다 정렬하여 투 포인터로 풀이
- 정렬에 ![image](https://user-images.githubusercontent.com/19264527/115976181-3490ef80-a5a6-11eb-93e6-6ced7005f009.png), 비교에 ![image](https://user-images.githubusercontent.com/19264527/115976185-4a9eb000-a5a6-11eb-830f-10b350796010.png) - 전체 풀이 ![image](https://user-images.githubusercontent.com/19264527/115976144-e7148280-a5a5-11eb-9954-1353a33cefd2.png)에 풀이

```python
# Runtime 48 ms / Memory 14.5 MB
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        # 양쪽 모두 정렬
        nums1.sort()
        nums2.sort()
        i = j = 0
        # 투 포인터 우측으로 이동하며 일치 여부 판별
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
                
        return result
```

 

### 실행 시간 비교

| 풀이 | 방식                         | 실행 시간 |
| ---- | ---------------------------- | --------- |
| 1    | 브루트 포스로 계산           | 148ms     |
| 2    | 이진 검색으로 일치 여부 판별 | 44ms      |
| 3    | 투 포인터로 일치 여부 판별   | 48ms      |
