# 13장 최단 경로 문제
## <a name='TOC'>목차</a>
0. [목차](#TOC)
1. [최단 경로 문제](#0)
2. [네트워크 딜레이 타임(Network Delay Time)](#1)
3. [K 경유지 내 가장 저렴한 항공권(Cheapest Flights Within K Stops)](#2)

## <a name='0'>최단 경로 문제</a>
### (1) [최단 경로 ](https://semaph.tistory.com/9)
- 내용
  - 정점 A에서 정점 B로 갈 때, 각 연결선에 주어진 가중치의 합이 최소인 경로를 찾는다.
  - 가중치 인접 행렬
    - 정점 간의 가중치 거리를 행렬로 나타낸 
    - 간선이 없을 때는 무한대(∞)로 표현한다. (가중치 자체가 0일 수 있으므로)
  - (보통)S: 최단 경로가 이미 찾아진 정점들의 집합
- 종류
  - 다익스트라 알고리즘
  - 벨만-포드 알고리즘
  - 플로이드-와샬 알고리즘
  - SPFA(Shortest Path Faster Algorithm)

### (2) [다익스트라 알고리즘 (Dijkstra's Algorithm)](https://mattlee.tistory.com/50)
- "최단 거리는 최단 거리로 이루어져 있다."
- ![image](https://user-images.githubusercontent.com/75566147/111031827-c73d5b00-844c-11eb-9e0b-2bd1bb0fe045.png)
- 구현 예시
  - 가능한 방식: 
    - 우선순위 큐(Priority Queue) : 추상 데이터타입, 기본 큐와 다르게 가장 높은 우선순위를 가진 요소가 먼저 나간다.
    - 힙(Heap) : 자료구조, 우선순위 큐 구현에 가장 적합하다. 완전 이진 트리(Complete Binary Tree), 최대 힙(Max Heap), 최소 힙(Min Heap) 등이 있다.
  - Pseudo Code
    - ```python3
      function Dijkstra(Graph, source):
          dist[source] = 0
          create vertex priority queue Q
          
          for each vertex v in Graph:
              if v != source:
                  dist[v] = INFINITY
                  prev[v] = UNDEFINED
              Q.add_with_priority(v, dist[v])  # 각 정점과 거리를 우선순위 큐에 삽입
              
          while Q is not empty:
              u = Q.extract_min()  # 우선순위 큐에서 최소값 추출
              for each neighbor v of u:  # 이웃한 정점들을 살펴본다
                  alt = dist[u] + length(u, v)
                  if alt < dist[v]:
                      dist[v] = alt
                      prev[v] = u
                      Q.decrease_priority(v, alt)
                      
          return dist, prev
      ```
  - 구현
    - [python의 heapq 모듈](https://www.daleseo.com/python-heapq/): 이진 트리 기반의 '최소 힙' 자료구조를 제공함
    - ```python3
      # 출처 : https://gist.github.com/kachayev/5990802
      from collections import defaultdict
      from heapq import *

      def dijkstra(edges, f, t):
          g = defaultdict(list)
          for l,r,c in edges:
              g[l].append((c,r))
          q, seen, mins = [(0,f,())], set(), {f: 0}
          while q:
              (cost,v1,path) = heappop(q)
              if v1 not in seen:
                  seen.add(v1)
                  path = (v1, path)
                  if v1 == t: return (cost, path)
                  for c, v2 in g.get(v1, ()):
                      if v2 in seen: continue
                      prev = mins.get(v2, None)
                      next = cost + c
                      if prev is None or next < prev:
                          mins[v2] = next
                          heappush(q, (next, v2, path))
          return float("inf"), None
      ```
### (3) [벨만-포드 알고리즘 (Bellman-Ford Algorithm)](https://victorydntmd.tistory.com/104)
- 음의 가중치를 가진 경로에서도 최단경로를 구할 수 있으며, 경로 추적이 가능함
### (4) [플로이드-와샬 알고리즘 (Floyd-Warshall Algorithm)](https://ssungkang.tistory.com/entry/Algorithm-%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%99%80%EC%83%ACFloyd-Warshall-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)
- 모든 정점 사이의 최단경로를 구할 수 있음
### (5) [SPFA (Shortest Path Faster Algorithm)](https://lemidia.github.io/algorithm/SPFA/)
- 벨만-포드 알고리즘을 개선한 알고리즘이지만, 음수 가중치가 없는 그래프의 경우에는 다익스트라 알고리즘이 더 적합하다고 함

## <a name='1'>#743 - 네트워크 딜레이 타임(Network Delay Time)</a>
### 문제
![image](https://user-images.githubusercontent.com/75566147/111032017-bb9e6400-844d-11eb-8efd-b380eda242e2.png)
### (1) 내 복붙 풀이
```python
from typing import List
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        weight_mat = collections.defaultdict(dict)

        # times의 [i, j, k]: i에서 j까지의 거리가 k
        # n : 노드의 수
        # k : 시그널을 보낼 노드 번호
        for start, end, distance in times:
            weight_mat[start][end] = distance
        # print(weight_mat)  # {2: {1: 1, 3: 1}, 3: {4: 1}}

        # 모든 n개의 노드가 시그널을 받을때까지 걸릴 시간은? (모든 노드가 시그널을 못 받는다면 -1을 리턴한다)
        heap = [(0, k)]  #
        dist = {}  # 시작점 기준, 다른 점까지의 최소 거리를 저장
        while heap:
            time, start = heapq.heappop(heap)
            if start not in dist:
                dist[start] = time
                for end in weight_mat[start]:
                    heapq.heappush(heap, (dist[start] + weight_mat[start][end], end))

        if len(dist) == n:
            return max(dist.values())
        else:
            return -1
```

### (2) 책 풀이
```python3
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 다익스트라 구현
        graph = collections.defaultdict(list)
        # 그래프 연결 리스트 구성
        for u, v, w, in times:
            graph[u].append((v, w))

        # 큐 변수: [(소요 시간, 정점)]
        Q = [(0, k)]
        dist = collections.defaultdict(int)

        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        return -1
```
- [Point](https://python.flowdas.com/library/heapq.html)
  - heapq.heappop(): 힙 불변성을 유지하면서, heap에서 가장 작은 항목을 팝하고 반환합니다. 힙이 비어 있으면, IndexError가 발생합니다. pop 하지 않고 가장 작은 항목에 액세스하려면, heap[0]을 사용하십시오.
  - heapq.heappush(): 힙 불변성을 유지하면서, item 값을 heap으로 푸시합니다.
  
### (3) 타인의 풀이 - 벨만-포드 알고리즘 사용
```python3
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [float("inf") for _ in range(N)]
        dist[K-1] = 0
        for _ in range(N-1):
            for u, v, w in times:
                if dist[u-1] + w < dist[v-1]:
                    dist[v-1] = dist[u-1] + w
        return max(dist) if max(dist) < float("inf") else -1
```

### (4) 타인의 풀이 - SPFA(Shortest Path Faster Algorithm) 사용
```python3
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [float("inf") for _ in range(N)]
        K -= 1
        dist[K] = 0
        weight = collections.defaultdict(dict)
        for u, v, w in times:
            weight[u-1][v-1] = w
        queue = collections.deque([K])
        while queue:
            u = queue.popleft()
            for v in weight[u]:
                if dist[u] + weight[u][v] < dist[v]:
                    dist[v] = dist[u] + weight[u][v]
                    queue.append(v)
        return max(dist) if max(dist) < float("inf") else -1
```

### (5) 타인의 풀이 - 플로이드-와샬 알고리즘 사용
```python3
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [[float("inf") for _ in range(N)] for _ in range(N)]
        for u, v, w in times:
            dist[u-1][v-1] = w
        for i in range(N):
            dist[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        return max(dist[K-1]) if max(dist[K-1]) < float("inf") else -1
```
  

## <a name='2'>#787 - K 경유지 내 가장 저렴한 항공권(Cheapest Flights Within K Stops)</a>
### 문제
![image](https://user-images.githubusercontent.com/75566147/111035909-ea253a80-845f-11eb-9290-7df584157a2a.png)
### (1) 내 풀이
```python3
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        weight_mat = collections.defaultdict(dict)
        for start, end, distance in flights:
            weight_mat[start][end] = distance

        # 최대 K개의 도시를 경유할 수 있을 때, src에서 dst까지의 최단 경로의 가격은? (없다면 -1 리턴)
        heap = [(0, src, 0)]  #
        dist = {}  # src 도시의 다른 도시까지의 가격을 저장한 dict
        max_stops = {}
        while heap:
            time, start, stops = heapq.heappop(heap)
            if start not in dist:
                dist[start] = time
                for end in weight_mat[start]:
                    if end not in max_stops:
                        max_stops[end] = stops
                    else:
                        max_stops[end] += 1
                    heapq.heappush(heap, (dist[start] + weight_mat[start][end], end, stops))

        if dst in max_stops.keys():
            if max_stops[dst] <= K:
                return dist[dst]
            else:
                if src in weight_mat.keys():
                    if dst in weight_mat[src].keys():
                        return weight_mat[src][dst]
                else:
                    return -1
        else:
            return -1

```
- 생각의 흐름
  - 앞선 문제와 유사하나, max_stops라는 경유한 도시 수를 저장하는 dict를 추가로 사용하고자 함.
- 평가
  - max_stops를 넣는 조건을 잘못 설정하여 막힘. 시간이 너무 지체되어 pass함

### (2) 책 풀이
```python3
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # 큐 변수: [(가격, 점, 남은 가능 경유지 수)]
        Q = [(0, src, K)]
        
        # 우선순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k-1))
         return -1
```
- Point
  - 경유한 도시의 수가 K개 이내일 때만 탐색을 계속 하도록 한다. 
  - 큐를 끝까지 돌아도 dst를 찾지 못하면 K 이내에 도착하는 경로는 존재하지 않으므로 -1을 리턴한다.
  - 거리를 보관할 필요가 없으므로 앞서 사용했던 dist 딕셔너리는 제거한다.


