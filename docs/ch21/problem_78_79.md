# 21장 그리디 알고리즘

### 그리디 알고리즘 (Greedy Algorithm)

- 글로벌 최적을 찾기 위해 각 단계에서 로컬 최적의 선택을 하는 휴리스틱 문제 해결 알고리즘
- 바로 눈 앞의 이익만 쫓는 알고리즘
- 최적화 문제를 대상으로 함. 
  - 최적해를 찾을 수 있다면 그것을 목표로 삼고, 찾기 어려운 경우에는 주어진 시간 내에 그런대로 괜찮은 해를 찾는 것을 목표

> **휴리스틱**(**heuristics**) 또는 발견법(發見法)이란 불충분한 시간이나 정보로 인하여 합리적인 판단을 할 수 없거나, 체계적이면서 합리적인 판단이 굳이 필요하지 않은 상황에서 사람들이 빠르게 사용할 수 있게 보다 용이하게 구성된 간편추론의 방법



### 그리디 알고리즘이 잘 작동하는 문제

- 탐욕 선택 속성을 갖고있는 최적 부분 구조인 문제
- 탐욕 선택 속성(Greedy Choice Property)
  - 앞의 선택 이후 선택에 영향을 주지 않는 것
  - 선택을 다시 고려하지 않는다
- 최적 부분 구조 (Optimal Substructure)
  - 문제의 최적 해결 방법이 부분 문제에 대한 최적 해결방법으로 구성되는 경우
- vs 다이나믹 프로그래밍 - 서로 반대 방향
  - 다이나믹 프로그래밍 - 하위 문제에 대한 최적의 솔루션을 찾은 다음 이 결과들을 결합한 정보에 입각해 전역 최적 솔루션에 대한 선택을 함
  - 그리디 - 각 단계마다 로컬 최적해를 찾는 문제로 접근해 문제를 더 작게 줄여나감

#### 배낭 문제

- 조합 최적화 분야의 매우 유명한 문제
- 배낭에 담을 수 있는 무게의 최대값이 정해져 있고 각 각 짐의 가치와 무게가 있는 짐들을 배낭에 넣을 때 가치의 합이 최대가 되도록 짐을 고르는 방법
- 짐을 쪼갤 수 있는 지 여부
  - 쪼갤 수 있음 - 그리디
    - 단가가 가장 높은 짐부터 차레대로 채워나가면 됨
  - 쪼갤 수 없음 - 다이나믹 프로그래밍

#### 동전 바꾸기 문제

- 동전의 액면이 10원, 50원, 100원 처럼 증가하면서 이전 액면의 배수 이상이 되면 그리디 알고리즘으로 풀 수 있음
  - 예) 160원 - 100원 1개, 50원 1개, 10원 1개
- 10, 50, 80, 100원 인 경우에는 그리디 알고리즘 적용 불가
  - 예) 160원 - 80 2개가 정답

#### 가장 큰 합 - 그리디 실패 사례

- 노드를 계속 더해나가다가 마지막으로 가장 큰 합이 되는 경우 찾기
- 간선으로 연결된 2가지 선택지 중 더 큰 수를 더해 나가면 될 것 같지만 정렬 등의 추가 작업 없이는 풀이 불가



## 78. 주식을 사고팔기 가장 좋은 시점 2

- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

>**122. Best Time to Buy and Sell Stock II** (Easy)
>
>You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.
>
>Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
>
>**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
>
> 
>
>**Example 1:**
>
>```
>Input: prices = [7,1,5,3,6,4]
>Output: 7
>Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
>Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
>```
>
>**Example 2:**
>
>```
>Input: prices = [1,2,3,4,5]
>Output: 4
>Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
>Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
>```
>
>**Example 3:**
>
>```
>Input: prices = [7,6,4,3,1]
>Output: 0
>Explanation: In this case, no transaction is done, i.e., max profit = 0.
>```
>
> 
>
>**Constraints:**
>
>- `1 <= prices.length <= 3 * 104`
>- `0 <= prices[i] <= 104`

- 여러 번의 거래로 낼 수 있는 최대 이익 산출
- 1일 때 사서 5일 때 팔아 4의 이익을 얻고, 3일 때 사서 6일 때 팔아 3의 이익을 얻는다.

  

### 1) 그리디 알고리즘

- 7장 12번 문제와는 여러번 거래할 수 있다는 차이가 있음
- 내리기 전에 팔고, 오르기 전에 사면 됨
  - 등락 여부를 미리 알 수 있음
  - 수수료가 없음
  - 항상 이익을 내는 방향으로 몇 번이든 사고 팔고 반복하며 매번 단계마다 이익을 취하는 탐욕 구조

```python
# 60ms / 14.9MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        # 값이 오르는 경우 매번 그리디 계산
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i+1] - prices[i]
        return result
```



### 2) 파이썬 다운 방식

- 매번 이익을 계산해 0보다 크면 무조건 합산

```python
# 60ms / 15.2MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0보다 크면 무조건 합산
        return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices)-1))
```



### 내 풀이

```python
# 56ms / 15MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                result += prices[i+1] - prices[i]
        return result
```

  

## 79. 키에 따른 대기열 재구성

- https://leetcode.com/problems/queue-reconstruction-by-height

>**406. Queue Reconstruction by Height** (Medium)
>
>You are given an array of people, `people`, which are the attributes of some people in a queue (not necessarily in order). Each `people[i] = [hi, ki]` represents the `ith` person of height `hi` with **exactly** `ki` other people in front who have a height greater than or equal to `hi`.
>
>Reconstruct and return *the queue that is represented by the input array* `people`. The returned queue should be formatted as an array `queue`, where `queue[j] = [hj, kj]` is the attributes of the `jth` person in the queue (`queue[0]` is the person at the front of the queue).
>
> 
>
>**Example 1:**
>
>```
>Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
>Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
>Explanation:
>Person 0 has height 5 with no other people taller or the same height in front.
>Person 1 has height 7 with no other people taller or the same height in front.
>Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
>Person 3 has height 6 with one person taller or the same height in front, which is person 1.
>Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
>Person 5 has height 7 with one person taller or the same height in front, which is person 1.
>Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
>```
>
>**Example 2:**
>
>```
>Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
>Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
>```
>
> 
>
>**Constraints:**
>
>- `1 <= people.length <= 2000`
>- `0 <= hi <= 106`
>- `0 <= ki < people.length`
>- It is guaranteed that the queue can be reconstructed.

 

### 1) 우선순위 큐 이용

- 우선순위 큐

  - 매번 그때 그때의 최소, 최댓값 추출
  - 그리디에 어울리는 대표적인 자료구조

  ```
  Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
  
  [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
  
  [[7,0]] 
  [[7,0],[7,1]]
  [[7,0],[6,1],[7,1]]
  [[5,0],[7,0],[6,1],[7,1]]
  [[5,0],[7,0],[5,2],[6,1],[7,1]]
  [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
  ```

- 첫 번째 값 - 큰 순서대로 추출되는 최대 힙(Max Heap)

  - 파이썬은 최소 힙만 지원하기 때문에 음수로 변경하여 풀이

- 두 번째 값 - 삽입되는 인덱스

   

####  전체 풀이

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        # 키 역순, 인덱스 삽입
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
            
        result = []
        # 키 역순, 인덱스 추출
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], (-person[0], person[1]))
        return result
```

