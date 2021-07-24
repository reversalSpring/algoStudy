# 14장 트리
## <a name='TOC'>목차</a>
0. [목차](#TOC)
1. [트리](#0)
2. [이진 트리의 최대 깊이(Maximum Depth of Binary Tree)](#1)
3. [이진 트리의 직경(Diameter of Binary Tree)](#2)

## <a name='0'>트리</a>
### (1) 용어
![image](https://user-images.githubusercontent.com/75566147/111039980-4eea9000-8474-11eb-9b89-5241f69b21c9.png)
### (2) 그래프 vs 트리
||그래프|트리|
|---|---|---|
|순환 구조|O|X|
|방향|단방향, 양방향|단방향|
|부모 노드의 수|>=1|1|
|루트의 수|>=1|1|
### (3) 이진 트리 : 모든 노드의 차수가 2 이하인 트리
|Full Binary Tree|Complete Binary Tree|Perfect Binary Tree|
|---|---|---|
![image](https://user-images.githubusercontent.com/75566147/111039849-97ee1480-8473-11eb-8332-5f14e3409c3a.png)|![image](https://user-images.githubusercontent.com/75566147/111039858-a0464f80-8473-11eb-8779-9ae998ab45d5.png)|![image](https://user-images.githubusercontent.com/75566147/111039860-a76d5d80-8473-11eb-9dc9-1126dc8c4d82.png)

## <a name='1'>#104 - 이진 트리의 최대 깊이(Maximum Depth of Binary Tree)</a>
### 문제
![image](https://user-images.githubusercontent.com/75566147/111039602-37120c80-8472-11eb-846f-485cf103ae0d.png)
### (1) 내 풀이
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        
        if root is None:
            return 0

        tree = [root]
        while tree:
            depth += 1
            next_round = []
            for node in tree:
                if node.left:
                    next_round.append(node.left)
                if node.right:
                    next_round.append(node.right)
            tree = next_round
            
        return depth
```
- Point
  - 계속해서 tree를 업데이트 해서 left나 right이 남아 있지 않을 때까지 탐색한다.

### (2) 책 풀이 - 반복 구조로 BFS 풀이
```python3
def maxDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    queue = collections.deque([root])
    depth = 0
    
    while queue:
        depth += 1
        # 큐 연산 추출 노드의 자식 노드 삽임
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
    # BFS 반복 횟수 == 깊이
    return depth
```
- Point
  - collections.deque([root])를 사용함
  - queue에 남아 있는 자식을 계속 추가함
  

## <a name='2'>#543 - 이진 트리의 직경(Diameter of Binary Tree)</a>
### 문제
![image](https://user-images.githubusercontent.com/75566147/111039613-43966500-8472-11eb-94cc-9eebae8e1611.png)
### (1) 내 풀이
```python3
# dfs를 떠올려 봄
def dfs(남은 애들):
    # 리프 노드일 때 결과 추가
    if 종료 조건:
        return 필요한 내용
        
    # 순열 생성 재귀 호출
    for e in 남은 애들:
        필요한 내용
        dfs(다음_애들)
```
```python3
class Solution:
    max_len = 0
    length_map = []

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(next_generation, depth, parent):
            # 리프 노드일 때 결과 추가
            # print(next_generation)                

            # 순열 생성 재귀 호출
            for e in next_generation:
                if e.left is None and e.right is None:
                    self.length_map.append(depth)
                    return
                depth += 1
                if e.left:
                    dfs([e.left], depth, e.val)
                if e.right:
                    dfs([e.right], depth, e.val)

        if root is None:
            return 0

        dfs([root], 0, root.val)
        self.length_map.sort()
        return (self.length_map.pop() + self.length_map.pop())
```
- Point
  - 맨 끝 노드에 도달할 때마다 length_map에 깊이를 저장하고, 이를 활용하고자 했으나...

### (2) 책 풀이 - 상태값 누적 트리 DFS
```python3
Class Solution:
    longest: int = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 가장 긴 경로
            self.longest = max(self.longest, left+right+2)
            # 상태값
            return max(left, right) + 1
        
        dfs(root)
        return self.longest
```
- Point
![image](https://user-images.githubusercontent.com/75566147/111062756-53ec2580-84ee-11eb-8ae3-592237ea55f8.png)
  - (상태값) = max(left, right) + 1
  - (거리) = (왼쪽 자식 노드의 리프부터 현재까지의 거리) + (오른쪽 자식 노드의 리프부터 현재 노드까지의 거리) + 2

### (3) [타인의 풀이 - global 변수 사용 없이](https://leetcode.com/problems/diameter-of-binary-tree/discuss/112275/Python-Simple-and-Logical-Idea)
```python3
Class Solution:
    def diameter_rec(self, root):
        # returns diameter, height at the current node
        if not root:
            return 0, 0

        left_diameter, left_height = self.diameter_rec(root.left)
        right_diameter, right_height = self.diameter_rec(root.right)
        curr_height = max(left_height, right_height) + 1
        # now current diameter will be max of left, diameter, right diameter or sum of left and right heights
        return max(left_diameter, right_diameter, left_height + right_height), curr_height
```

### (4) [타인의 풀이 - 재귀 사용 없이](https://leetcode.com/problems/diameter-of-binary-tree/discuss/133736/iterative-and-recursive-python-solutions)
```python3
class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_length = 0
        depth = {None: -1}
        stack = [(root, 0)]
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if visited == 0:
                stack.extend([(node, 1), (node.left, 0), (node.right, 0)])
            else:
                left_d = depth[node.left] + 1
                right_d = depth[node.right] + 1
                depth[node] = max(left_d, right_d)
                max_length = max(max_length, left_d + right_d)
        return max_length
```

