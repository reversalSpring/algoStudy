# 12장 그래프

*38 일의 재구성*

problem
```
[form, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라.
여러 일정이 있는 경우 사전 어휘 순[lexical Order]으로 방문한다.
```

Example 1:
```
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
```
Example 2:
```
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
```
### 풀이
1. tickets 이 빈값인지 체크
2. tickets 출발, 목적지에 따라 route에 얺어준다.
3. 순서대로 나오기 위하여 역순으로 정렬
4. 만약 키가 있다면 값을 꺼낸다.
5. 다쓴 키 값은 삭제
6. 남은 키가 없을 때 까지 반복

```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        if not tickets:
            return []
        
        route = {}
        for i in tickets:
            start, end = i[0], i[1]
            if start in route:
                route[start].append(end)
            else:
                route[start] = [end]
                
        for z, k in route.items():
            k.sort(reverse=True)
            
        print(route)
        
        sol = []
        cur = 'JFK'
        while route:
            if cur in route:
                sol.append(cur)
                next = route[cur].pop()
                if not route[cur]:
                    del route[cur]
                cur = next
                
        sol.append(cur)
        
        return sol
```

*207. Course Schedule*

### problem
```
0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0,1] 쌍으로 표현하는 n개의 코스가 있다.
코스 개수 n과 이 쌍들을 입력으로 받았을 때 모든 코스가 완료 가능한지 판별하라.
```

Example 1
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
```

Example 2

```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

### 책 풀이

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        #그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)
            
        traced = set()
        visited = set()
        
        def dfs(i):
            #순환 구조이면 False
            if i in traced:
                return False
            #이미 방문했던 노드이면 False
            if i in visited:
                return True
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
                
            #탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            #탐색 종료 후 방문 노드 추가
            visited.add(i)
            
            return True
        
        #순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False
            
        return True
```
