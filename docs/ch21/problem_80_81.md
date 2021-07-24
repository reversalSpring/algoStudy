# 21장 그리디 알고리즘
## <a name='TOC'>목차</a>
0. [목차](#TOC)
2. [태스크 스케줄러 (Task Scheduler)](#1)
3. [주유소 (Gas Station)](#2)


## <a name='1'>[#621 - 태스크 스케줄러 (Task Scheduler)](https://leetcode.com/problems/task-scheduler/)</a>
### 문제
![image](https://user-images.githubusercontent.com/75566147/120098496-40f20480-c171-11eb-8f2e-d9601ea1bb71.png)


### (1) 내 풀이
```python3
class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        step, hq = 0, []
        for k, v in Counter(tasks).items():
            heapq.heappush(hq, (1 * v, k))

        while hq:
            i = 0
            returning_list = []
            while i <= n:                                       # 이 while문 한 번이 쿨타임 한 번
                step += 1
                if hq:
                    ind, val = heapq.nlargest(1, hq)[0]         # 개수가 가장 많은 프로세스를 들고 온다
                    hq.remove((ind, val))
                    if ind != 1:                                # 2개 이상 존재하는 프로세스라면
                        returning_list.append((ind - 1, val))   # 개수가 남은 아이들은 나중에 다시 hq로 돌려주기 위해 returning_list에 넣음
                        
                if not hq and not returning_list:
                    break
                else:
                    i += 1
            hq.extend(returning_list)                           # returning_list에 있던 애들을 hq로 다시 집어넣는다
            
        return step
```
- Point
  - n이라는 간격 안에 동일한 프로세스가 있지만 않으면 된다.
  - 즉, 프로세스 간에 우선순위가 존재하지 않으므로 tasks에서 unique한 프로세스라면 아무거나 non-unique한 애들 다음에 들어가면 된다는 뜻

### (2) 책 풀이 - 우선순위 큐 이용
```python3
class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0
        
        while True:
            sub_count = 0
            for tasks, _ in counter.most_common(n+1):    # n이 아닌 (n+1)을 사용하여 예외 처리를 할 필요가 없음
                sub_count += 1
                result += 1
                
                counter.subtract(tasks)                  # 사용된 프로세스는 개수를 하나 줄임
                counter += collections.Counter()         # 0개 이하인 프로세스를 목록에서 완전히 제거
                
            if not counter:
                break
            
            result += n - sub_count + 1                  # (n+1) - sub_count: 'idle'이 빠진 수만큼 채워준다
        
        return result
```
- Point
  - heapq 모듈의 한계점을 보완하기 위해 Counter 모듈을 사용
  - counter.most_common(n+1)을 사용하여 'idle'을 사용하지 않는 대신 result += n - sub_count + 1 을 통해 수치 보정을 함

### (3) [타인의 풀이](https://leetcode.com/problems/task-scheduler/discuss/1154618/Python-Easiest-without-heaps-and-PQ.-Beats-90-Time-95-Space)
```python3
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        size = len(tasks)
        c = Counter(tasks)
        most_common, num = c.most_common(1)[0]      # most_common: 가장 많은 프로세스, num: 그것의 개수
        max_c = 0
        
        for i in c:                                 # 가장 개수가 많은 프로세스부터 순서대로
            if c[i] == num:
                max_c += 1                          # 가장 개수가 많은 프로세스의 수 (여러 개일 수도 있음 ex.AAABBBCD)
        
        return max(size, max_c + (n+1)*(num-1))     # tasks의 수보다 적게 나올 때가 있는데 이것을 방지하기 위해 max(size, 식)으로 계산
```
- Point
  - 이 풀이도 초점은 '가장 많이 나온 프로세스의 수'
  - 식 : (가장 많이 나온 프로세스의 수 - 1)x(n+1) + remain(코드에서 max_c)
  - detailed explanation : https://shawnlyu.com/leetcode/leetcode621-task-scheduler/

### (4) 성능 비교
||방식|실행 시간(ms)|
|---|---|---|
|나|heapq 사용|842|
|책|우선순위 큐 이용|1308|
|기타|규칙 파악|396|




## <a name='2'>[#134 - 주유소 (Gas Station)](https://leetcode.com/problems/gas-station/)</a>
### 문제
![image](https://user-images.githubusercontent.com/75566147/120098511-49e2d600-c171-11eb-89b4-c0df8d2d4fca.png)

### (1) 내 풀이
```python3
from collections import Counter, deque

class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        dq = deque()
        for i in range(n):
            dq.append((i, gas[i], cost[i]))             # dq[i][1]은 그 주유소에서 받는 연료량, dq[i][2]은 다음까지 가는데 필요량

        for i in range(n):                              # i번째 주유소를 고정
            my_tank = gas[i] - cost[i]
            if my_tank < 0:
                continue
            dq.rotate(-(i+1))                           # i번째 다음 주유소가 dq의 제일 앞에 오도록 회전
            for item in dq:                             # 나머지 주유소에 순서대로 간다.
                if item[0] == i:                        # 출발지로 다시 돌아오면 성공
                    return i
                my_tank = my_tank + item[1] - item[2]   # 현재 연료량 - 다음까지 가는데 필요한 양 + 다음에서 받는 양
                if my_tank < 0:                         # 연료가 부족하므로 이 경로를 더 탐색하는 것은 무의미하다
                    break
            dq.rotate((i+1))                            # dq를 원래대로 되돌림
            
        return -1                                       # 정답을 찾지 못하고 빠져나오면 -1 리턴
```
- Point
  - 브루트 포스 방법 + dq로 원형 경로를 표현
  - i번째 주유소를 고정하고, dq에서 (i+1)번째 주유소에서부터 순서대로 돌며 다시 출발지(i번째 주유소)로 돌아오면 성공
  - 출발지로 돌아오지 못하고 빠져나오면 -1 반환

### (2) 책 풀이 1 - 모두 방문
```python3
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for start in range(len(gas)):
            fuel = 0
            for i in range(start, len(gas)+start):
                index = i % len(gas)                        # 순환을 구현하기 위해 % 를 넣음
            
                can_travel = True
                if gas[index] + fuel < cost[index]:
                    can_travel = False
                    break
                else:
                    fuel += gas[index] - cost[index]
        
            if can_travel:
                return start
        return -1
```
- Point
  - 순환을 구현하기 위해 % 를 넣음 (deque() 미사용)
  - 0번째 주유소부터 순서대로 출발점으로 지정하고, 나머지 주유소를 전부 방문

### (3) 책 풀이 2 - 한 번 방문
```python3
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 모든 주유소 방문 가능 여부 판별
        if sum(gas) < sum(cost):
            return -1
        
        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발점이 안 되는 지점 판별
            if gas[i] + fuel < cost[i]:
                start = i+1                      # 다음 주유소로 갈 수 없다면, 바로 출발점을 바꾼다
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start
```
- Point
  - 도입부의 if문: 절대로 불가능한 케이스일 경우 불필요한 연산을 하지 않고 바로 -1을 리턴하도록 하는 장치
  - 문제에서 경로가(출발점이) 유일하다고 알려줬기 때문에 도입부의 if문을 통과하면 반드시 출발점이 존재하고, 출발점은 유일하므로 전체 주유소를 한 번만 돌며 확인하면 충분하다는 로직

### (4) 성능 비교
||방식|실행 시간(ms)|
|---|---|---|
|나|모두 방문 + deque() 사용|2640|
|책|모두 방문 + % 사용|4680|
|책|한 번 방문|56|

끝.

