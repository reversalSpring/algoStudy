# 12장 그래프
## <a name='TOC'>목차</a>
0. [목차](#TOC)
1. [순열(Permutations)](#p)
2. [조합(Combinations)](#c)

## 순열과 조합 [(출처)](https://coding-factory.tistory.com/606)
![image](https://user-images.githubusercontent.com/75566147/109409259-9a149580-79d4-11eb-8558-dd8d4b5b1753.png)


## <a name='p'>#46 - 순열(Permutations)</a> 
### (1) 내 풀이
```python
from Typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # FYI- 순열 : 서로 다른 n개의 수에서 중복이 없게 r개를 택하여 일렬로 배열하는 것
        def dfs(index, path):
            if path is not None and len(path) == len(nums):
                result.append(path)
                return

            for i in range(index, len(nums)):
                for j in nums:
                    if j not in path:  # 중복되는 숫자가 없도록
                        dfs(i+1, path+[j])

        result = []
        dfs(0, [])
        return result
```
- Point
  - 앞서 33번 문제와 사실상 굉장히 
- 평가
  - Runtime: **48 ms, faster than 20.49%** of Python3 online submissions for Permutations.
  - Memory Usage: **14.5 MB, less than 16.44%** of Python3 online submissions for Permutations.

### (2) 책 풀이 1 - DFS를 활용한 순열 생성
```python3
def permute(self, nums: List[int]) -> List[List[int]]:
    results = []
    prev_elements = []
    
    def dfs(elements):
        # 리프 노드일 때 결과 추가
        if len(elements) == 0:
            results.append(prev_elements[:])  # 값을 복사하는 형태로
    
        # 순열 생성 재귀 호출
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)
            
            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()
    
    dfs(nums)
    return results
```
- Point
  - ![image](https://user-images.githubusercontent.com/75566147/109410689-0648c680-79e0-11eb-8744-d8f9eafa7c8b.png)
  
### (3) 책 풀이 2 - itertools 모듈 사용
```python3
def permute(self, nums: List[int]) -> List[List[int]]:
    return list(map(list, itertools.permutations(nums)))
```
- Point
  - itertools 모듈 사용
  - itertools.permutations() 함수가 튜플 모음을 반환하기 때문에, 리스트 형태로 변형 필요
  - print(itertools.permutations(nums)) 는 <itertools.permutations object at 0x000001A22FDEE590>
  - print(map(list, itertools.permutations(nums))) 는 <map object at 0x000001A22FDD8790>

### (4) 타인의 풀이 - [출처](https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS).)
```python3
def permute(self, nums: List[int]) -> List[List[int]]:
    res = []
    self.dfs(nums, [], res)
    return res
    
def dfs(self, nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    for i in range(len(nums)):
        self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
```
- Point
  - 책 풀이 1과 동일한 로직이지만 구현 방법만 다름
  

## <a name='c'>#77 - 조합(Combinations)</a>
### (1) 내 풀이 - 1 : Timeout 남
```python3
import math
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # nCk = n!/k!*(n-k)!
        def dfs(path):
            if len(path) == k:
                path.sort()  # 야메.. 더 좋은 방법 떠오르면 대체하겠음
                if path not in result:
                    result.append(path)
                    return

            for i in range(1, n + 1):
                for j in range(i, n + 1):
                    if j not in path:  # 중복되는 숫자가 없도록
                        if len(result) == limit:
                            return
                        else:
                            dfs(path + [j])

        result = []
        limit = math.factorial(n) / (math.factorial(n - k) * math.factorial(k))
        dfs([])

        return result
```
- 생각의 흐름
  - 순열 코드에 k개 제한과 중복을 제한하는 코드만 덧붙임
- 평가
  - 결과는 책 풀이와 동일한 것을 확인했으나, Timeout이 나서 사실상 아무 소용이 없음

### (2) 책 풀이 1 - DFS로 k개 조합 생성
```python3
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        
        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return
            
            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
        
        dfs([], l, k)
        return results
```
- Point
  - ![image](https://user-images.githubusercontent.com/75566147/109411697-46f80e00-79e7-11eb-9b62-a4caa34160ea.png)
  

### (3) 책 풀이 2 - itertools 모듈 사용
```python3
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1), k))
```
- Point
  - itertools 모듈 사용
  - itertools.combinations()를 사용함(풀이 1보다 훨씬 빠름)
- (itertools 공식 문서)[https://docs.python.org/ko/3.8/library/itertools.html]

