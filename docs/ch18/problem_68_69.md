# 18장 이진 검색
## <a name='TOC'>목차</a>
0. [목차](#TOC)
2. [두 수의 합 Ⅱ (Two Sum Ⅱ - Input array is sorted)](#1)
3. [2D 행렬 검색 Ⅱ (Search a 2D Matrix Ⅱ)](#2)


## <a name='1'>[#167 - 두 수의 합 Ⅱ (Two Sum Ⅱ - Input array is sorted)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)</a>
### 문제
![image](https://user-images.githubusercontent.com/75566147/116780217-29fabc80-aab6-11eb-9754-a2f0c9a87cee.png)

### (1) 내 풀이
```python3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def bs(left, right, leftover):
            if left <= right:
                mid = (left + right) //2
                if numbers[mid] < leftover:
                    return bs(mid+1, right, leftover)
                elif numbers[mid] > leftover:
                    return bs(left, mid-1, leftover)
                else:
                    return mid
            else:
                return -1
        
        answer = list()
        for i in range(0, len(numbers)):
            index = bs(i+1, len(numbers)-1, target-numbers[i])
            if index != -1:
                answer.append(i+1)
                answer.append(index+1)
                    
        return answer
```
- Point
  - numbers에 대해 반복문을 돌리면서 원소 하나를 고정해두고, 리스트 나머지 원소에 대해 target이 있는지 binary search를 돌린다.

### (2) 책 풀이 - 투 포인터
```python3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) -1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left+1, right+1
```
- Point
  - 리스트의 양 끝에서부터 하나씩 범위를 좁혀 오는 방법

### (3) 책 풀이 - 이진 검색
```python3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k+l, len(numbers)-1
            expected = target - v
            # 이진 검색으로 나머지 값 판별
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k+1, mid+1
```
- Point
  - 값 하나를 고정해놓고, 이진 탐색을 통해 리스트의 나머지 원소들 중 알맞은 값을 찾는 방법
  - for k, v in enumerate(리스트) : 리스트의 인덱스(k)와 값(v)을 쌍으로 넘김

### (4) 책 풀이 - bisect 모듈 + 슬라이싱
```python3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers[k+1:], expected)
            if i < len(numberts[k+1:]) and numbers[i+k+1] == expected:
                return k+1, i+k+2        
```
- Point
  - ![image](https://user-images.githubusercontent.com/75566147/116780852-0df91a00-aaba-11eb-955f-096cd210a6df.png)
  - [bisect 모듈](https://docs.python.org/ko/3/library/bisect.html)
    - ```python3
      from bisect import bisect_right, bisect_left

      a = [1,2,3,4,8]
      x = 4

      print(bisect_left(a,x))  # 3
      print(bisect_right(a,x))  # 4
      ```
    - ```python3
      from bisect import bisect_right, bisect_left

      a = [1,2,3,4,4,8]
      x = 4

      print(bisect_left(a,x))  # 3
      print(bisect_right(a,x))  # 5
      ```
    - bisect.bisect_xxx() 함수들은 전부 주어진 시퀀스의 **정렬된 순서를 유지**하며 탐색하고, **찾지 못하면 -1**을 리턴
    - **bisect.bisect_left(a, x, 시작ind, 종료ind)** : 시퀀스 a에 데이터 x 와 동일한 값의 **가장 왼쪽 인덱스** 찾기
    - **bisect.bisect_right(a, x, 시작ind, 종료ind)** : 시퀀스 a에 데이터 x 와 동일한 값의 **가장 오른쪽 인덱스+1** 찾기
    - bisect.bisect() : bisect_right()와 동일
    - [문제풀이에 활용한 예시](https://velog.io/@woo0_hooo/python-Bisect-%ED%95%A8%EC%88%98%EB%9E%80)

### (5) 책 풀이 - bisect 모듈 + 슬라이싱 최소화
```python3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            nums = numbers[k+1:]
            i = bisect.bisect_left(nums, expected)
            if i < len(nums) and numbers[i+k+1] == expected:
                return k+1, i+k+2        
```

### (6) 책 풀이 - bisect 모듈 + 슬라이싱 제거
```python3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k+1)
            if i < len(numbers) and numbers[i] == expected:
                return k+1, i+l        
```
- Point
  - 슬라이싱을 제거하자 속도 저하 현상이 해결되었다.

### (7) 성능 비교
||방식|실행 시간(ms)|
|---|---|---|
|나|이진 검색|156|
|책|투 포인터|68|
|책|이진 검색|112|
|책|bisect 모듈 + 슬라이싱|2184|
|책|bisect 모듈 + 슬라이싱 최소화|1136|
|책|bisect 모듈 + 슬라이싱 제거|68|



## <a name='2'>[#240 - 2D 행렬 검색 Ⅱ (Search a 2D Matrix Ⅱ)](https://leetcode.com/problems/merge-intervals/)</a>
### 문제
![image](https://user-images.githubusercontent.com/75566147/116780225-397a0580-aab6-11eb-9bfd-2a46a3e8f4c9.png)

### (1) 내 풀이
```python3
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = -1
        
        def bs(arr, left, right):
            if left <= right:
                mid = (left+right) // 2
                
                if arr[mid] < target:
                    return bs(arr, mid+1, right)
                elif arr[mid] > target:
                    return bs(arr, left, mid-1)
                else:
                    return mid
            else:
                return -1
        
        
        for row in matrix:
            if row[0] <= target:
                index = bs(row, 0, len(row)-1)
                if index != -1:
                    return True
        
        return False
```
- Point
  - 주어진 matrix에 대해 반복문을 돌려서, 각 행마다 첫 element가 target보다 작을 때만 그 행에 binary search를 돌려서 target이 있는 곳을 찾아낸다.
  - ![image](https://user-images.githubusercontent.com/75566147/116780869-22d5ad80-aaba-11eb-83b3-e59623b618c8.png)

### (2) 책 풀이 - 첫 행의 맨 뒤에서 탐색
```python3
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 예외 처리
        if not matrix:
            return False
        
        # 첫 행의 맨 뒤
        row = 0
        col = len(matrix[0]) - 1
        
        while row <= len(matrix)-1 and col>=0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 왼쪽으로 이동
            elif target < matrix[row][col]:
                col -= 1
            # 타겟이 크면 아래로 이동
            elif target > matrix[row][col]:
                row += 1
        return False
```
- Point
  - ![image](https://user-images.githubusercontent.com/75566147/116780874-249f7100-aaba-11eb-8641-a94681fc36b4.png)

### (3) 책 풀이 - 파이썬다운 방식
```python3
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)
```
- Point
  - any() 함수
    - 인자로 반복 가능한 자료형(리스트, 튜플, 집합, 딕셔너리, 문자열)을 받음
    - True 인 경우 : 인자의 원소 중 하나라도 True일 때
    - False 인 경우 : 인자가 비어 있거나, 모든 원소가 False일 때  
  - all() 함수
    - 인자로 반복 가능한 자료형(리스트, 튜플, 집합, 딕셔너리, 문자열)을 받음
    - True인 경우 : 인자의 모든 원소가 True이거나, 인자가 비어 있을 때
    - False인 경우 : 인자의 원소 중 하나라도 False일 때

### (4) 성능 비교
||방식|실행 시간(ms)|
|---|---|---|
|나|각 행의 첫 원소와 비교 후 탐색 결정|164|
|책|첫 행의 맨 뒤에서 탐색|36|
|책|파이썬다운 방식|36|

끝.

