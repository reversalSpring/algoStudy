## 0-1 배낭 문제

- 짐을 쪼갤 수 없는 배낭 문제
- '탐욕 선택 속성' X, '중복된 하위 문제들' 속성 -> 다이나믹 프로그래밍
- 짐을 쪼갤 수 없기 때문에 모든 경우의 수 계산
  - 다이나믹 프로그래밍 위력 발휘
- 타뷸레이션 이용
  - 테이블 크기 - 짐의 최대 개수 + 1 X 배낭의 최대 용량 + 1 => 6 X 16
  - 테이블 각 셀에는 그 위치 까지의 짐의 개수와 배낭의 용량에 따른 최대값이 담김
  - 최악의 경우 O(2^n) 에서 O(nW) n - 짐의 개수 / W - 배낭의 용량 으로 풀이 가능

```python
cargo = [
  (4, 12),
  (2, 1),
  (10, 4),
  (1, 1),
  (2, 2),
]
r = zero_one_knapsack(cargo)

def zero_one_knapsack(cargo):
  capacity = 15
  pack = []
  
  for i in range(len(cargo) + 1):
    pack.append([])
    for c in range(capacity + 1):
      if i == 0 or c == 0:
        pack[i].append(0)
        
      elif cargo[i - 1][1] <= c:
        pack[i].append(
       		max(
            cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
            pack[i - 1][c]
          )
        )
      else:
        pack[i].append(pack[i - 1][c])
        
  return pack[-1][-1]
```



## 86. 최대 서브 배열

- https://leetcode.com/problems/maximum-subarray/

>**53. Maximum Subarray** (Easy)
>
>Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return *its sum*.
>
> 
>
>**Example 1:**
>
>```
>Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
>Output: 6
>Explanation: [4,-1,2,1] has the largest sum = 6.
>```
>
>**Example 2:**
>
>```
>Input: nums = [1]
>Output: 1
>```
>
>**Example 3:**
>
>```
>Input: nums = [5,4,-1,7,8]
>Output: 23
>```
>
> 
>
>**Constraints:**
>
>- `1 <= nums.length <= 3 * 104`
>- `-105 <= nums[i] <= 105`

  

### 1) 메모이제이션

- 이 문제는 투포인터 풀이로는 어렵
  - 연속된 서브배열을 찾아야하는 만큼, 정렬을 할 수 없고 다음 숫자가 뭐가 될지 모르는 상황에서 단순히 음수를 건너뛰는 방식으로는 구현이 어려움
  - 투포인터로 풀이하기 위해서는 정렬 필요

- 메모이제이션 이용
  - 앞에서부터 계속 값을 계산하면서 누적 합을 계산
  - 이전 값을 계속 더해나가되, 0 이하가 되면 버린다
  - 메모이제이션으로 값을 더해나간 sums에서 최댓값 추출하면 서브 배열의 최댓값 추출 가능

```python
# 60ms / 15MB
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)
```



### 2) 카데인 알고리즘

- 이 문제는 1977년에 제안된 유명한 컴퓨터 과학 알고리즘 문제
- 카데인 알고리즘(Kadane's Algorithm) - 제이 카데인(Jay Kadane)이  이 문제를 O(n)에 풀이 가능하도록 고안한 해법
- 각 단계마다 매번 최댓값을 담아 어디서 끝나는지를 찾는 방식
- 1번과 사실상 동일

 ```python
# 148ms / 14.0MB
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        
        return best_sum
 ```

  

## 87. 계단 오르기

- https://leetcode.com/problems/climbing-stairs/

>**70. Climbing Stairs** (Easy)
>
>You are climbing a staircase. It takes `n` steps to reach the top.
>
>Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?
>
> 
>
>**Example 1:**
>
>```
>Input: n = 2
>Output: 2
>Explanation: There are two ways to climb to the top.
>1. 1 step + 1 step
>2. 2 steps
>```
>
>**Example 2:**
>
>```
>Input: n = 3
>Output: 3
>Explanation: There are three ways to climb to the top.
>1. 1 step + 1 step + 1 step
>2. 1 step + 2 steps
>3. 2 steps + 1 step
>```
>
> 
>
>**Constraints:**
>
>- `1 <= n <= 45`

 

### 1) 재귀 구조 브루트 포스

- 피보나치 수와 동일한 유형의 문제
- 재귀로 풀이

```python
# Time Limit Exceeded
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
```



### 2) 메모이제이션

- 피보나치 수와 초깃값만 약간 다를 뿐 메모이제이션으로 풀이하는 방식 동일

```python
# 36ms / 14.2MB
class Solution:
    dp = collections.defaultdict(int)
    
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]
```

