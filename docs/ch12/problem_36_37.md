## 36. 조합의 합

- https://leetcode.com/problems/combination-sum/

>**39. Combination Sum** (Medium)
>
>Given an array of **distinct** integers `candidates` and a target integer `target`, return *a list of all **unique combinations** of* `candidates` *where the chosen numbers sum to* `target`*.* You may return the combinations in **any order**.
>
>The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
>
>It is **guaranteed** that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.
>
>**Example 1:**
>
>```
>Input: candidates = [2,3,6,7], target = 7
>Output: [[2,2,3],[7]]
>Explanation:
>2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
>7 is a candidate, and 7 = 7.
>These are the only two combinations.
>```
>
>**Example 2:**
>
>```
>Input: candidates = [2,3,5], target = 8
>Output: [[2,2,2,2],[2,3,3],[3,5]]
>```
>
>**Example 3:**
>
>```
>Input: candidates = [2], target = 1
>Output: []
>```
>
>**Example 4:**
>
>```
>Input: candidates = [1], target = 1
>Output: [[1]]
>```
>
>**Example 5:**
>
>```
>Input: candidates = [1], target = 2
>Output: [[1,1]]
>```
>
> 
>
>**Constraints:**
>
>- `1 <= candidates.length <= 30`
>- `1 <= candidates[i] <= 200`
>- All elements of `candidates` are **distinct**.
>- `1 <= target <= 500`

### 1)  DFS로 중복 조합 그래프 탐색

- 순열이 아닌 조합이기 때문에 매번 처음부터 시작하지 않고, 자기 자신부터 하위 원소까지의 나열로만 정리

  ```python
  def dfs(csum, index, path):
      ...
      for i in range(index, len(candidates)):
          dfs(csum - candidates[i], i, path + [candidates[i]])
  ```

- `dfs()` 함수 파라미터

  1. 합을 갱신해나갈 csum
  2. 자기 자신을 포함하는 index 순서
  3. 현재까지 탐색 경로

- 탐색 재귀 종료 조건

  1. `csum < 0` : 목표값을 초과하는 경우
  2. `csum = 0` : `csum`의 초기값은 `target`이며, `csum` 의 0은 `target`과 일치하는 정답이므로 결과 리스트에 추가하고 탐색을 종료

  ```python
  def dfs(csum, index, path):
      if csum < 0:
          return
      if csum == 0:
          result.append(path)
          return
      ...
  ```



#### 내 풀이

```python
# Runtime 84 ms / Memory 14.5 MB
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(index, sum, path):
            if sum == target:
                result.append(path)
                return
            
            if sum > target:
                return
            
            for i in range(index, len(candidates)):
                dfs(i, sum + candidates[i], path + [candidates[i]])
                
        dfs(0, 0, [])
        return result
```

  

#### 전체 풀이

```python
# Runtime 80 ms / Memory 14.4 MB
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return
            
            # 자신부터 하위 원소까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
                
        dfs(target, 0, [])
        return result
```

   

## 37. 부분 집합

- https://leetcode.com/problems/subsets/

>**78. Subsets** (Medium)
>
>Given an integer array `nums` of **unique** elements, return *all possible subsets (the power set)*.
>
>The solution set **must not** contain duplicate subsets. Return the solution in **any order**.
>
>**Example 1:**
>
>```
>Input: nums = [1,2,3]
>Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
>```
>
>**Example 2:**
>
>```
>Input: nums = [0]
>Output: [[],[0]] 
>```
>
>**Constraints:**
>
>- `1 <= nums.length <= 10`
>- `-10 <= nums[i] <= 10`
>- All the numbers of `nums` are **unique**.

### 1)  트리의 모든 DFS 결과

- 경로 path를 만들어 나가면서 인덱스를 1씩 증가시키는 형태로 깊이 탐색 

  - 별도의 종료 조건 필요 없음

  ```python
  def dfs(index, path):
      ...
      for i in range(index, len(nums)):
          dfs(i + 1, path + [nums[i]])
  ```

- 부분 집합은 모든 탐색의 경로가 결국 정답 - 탐색할 때마다 매번 결과를 추가

  ```python
  def dfs(index, path):
      ...
      result.append(path)
  ```



#### 전체 풀이

```python
# Runtime 32 ms / Memory 14.4 MB
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(index, path):
            # 매번 결과 추가
            result.append(path)
            
            # 경로를 만들면서 DFS
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
                
        dfs(0, [])
        return result
```