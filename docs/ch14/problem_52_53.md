## 52. 이진 탐색 트리(BST) 합의 범위

- https://leetcode.com/problems/range-sum-of-bst/

>**938. Range Sum of BST** (Easy)
>
>Given the `root` node of a binary search tree, return *the sum of values of all nodes with a value in the range `[low, high]`*.
>
> 
>
>**Example 1:**
>
>![img](https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg)
>
> ```
>Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
>Output: 32
>```
>
>**Example 2:**
>
>![img](https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg)
>
>```
>Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
>Output: 23
>```
>
> 
>
>**Constraints:**
>
> - The number of nodes in the tree is in the range `[1, 2 * 104]`.
>- `1 <= Node.val <= 105`
>- `1 <= low <= high <= 105`
>- All `Node.val` are **unique**.

  

### 1) 재귀 구조 DFS로 브루트 포스 탐색

1. DFS로 전체를 탐색
2. 노드의 값이 L과 R 사이일 때만 값 부여, 아닐 경우 0
3. 계속 더해나가기 

```python
# Runtime 284 ms / Memory 22.3 MB
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        
        return (root.val if L <= root.val <= R else 0) 
      + self.rangeSumBST(root.left, L, R) 
      + self.rangeSumBST(root.right, L, R)
```

  

### 2) DFS 가지 치기로 필요한 노드 탐색

- DFS로 탐색하되, L, R 조건에 해당되지 않는 가지를 쳐내는 형태로 탐색 (Pruning)
- 이진트리는 왼쪽이 항상 작고, 오른쪽이 항상 크다.
  - 현재 노드가  L보다 작을 경우 더 이상 왼쪽 가지는 탐색할 필요가 없다.
  - 현재 노드가  R보다 클 경우 더 이상 오른쪽 가지는 탐색할 필요가 없다.

```python
# Runtime 268 ms / Memory 22.4 MB
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0
            
            if node.val < L:
                return dfs(node.right)
            elif node.val > R:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)
        
        return dfs(root)
```

  

### 3) 반복 구조 DFS로 필요한 노드 탐색

- 대부분의 재귀 풀이는 반복으로 변경 가능
- 반복 풀이가 재귀 풀이보다 좀 더 직관적
- 유효한 노드만 스택에 계속 집어 넣으면서, L과 R사이의 값인 경우 값을 더해 나간다. (가지치기와 탐색 범위 유사)

```python 
# Runtime 192 ms / Memory 22.1 MB
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack, sum = [root], 0
        # 스택 이용 필요한 노드 DFS 반복
        while stack:
            node = stack.pop()
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    sum += node.val
        return sum
```

  

### 4) 반복 구조 BFS로 필요한 노드 탐색

- DFS의 스택을 큐의 형태로 변경
- 파이썬의 데크를 사용하면 성능을 높일 수 있음.
- 반복 풀이가 재귀 풀이보다 좀 더 직관적
- 유효한 노드만 스택에 계속 집어 넣으면서, L과 R사이의 값인 경우 값을 더해 나간다. (가지치기와 탐색 범위 유사)

```python
# Runtime 212 ms / Memory 22.6 MB
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack, sum = [root], 0
        # 스택 이용 필요한 노드 DFS 반복
        while stack:
            node = stack.pop(0)
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    sum += node.val
        return sum
```

​      

### 실행 시간 비교

- 테스트 케이스의 입력값이 컸다면?
  -  브루트 포스와 가지치기의 실행시간 차이가 클 것
  - BFS 구현에서 `pop(0)` 은 O(n)이기 때문에  DFS와 구현 속도 차이가 많이 날 것

| 풀이 | 방식                             | 실행 시간 |
| ---- | -------------------------------- | --------- |
| 1    | 재귀 구조 DFS로 브루트 포스 탐색 | 288ms     |
| 2    | DFS 가지 치기로 필요한 노드 탐색 | 224ms     |
| 3    | 반복 구조 DFS로 필요한 노드 탐색 | 220ms     |
| 4    | 반복 구조 BFS로 필요한 노드 탐색 | 232ms     |

  

#### 내 풀이

```python
# Runtime 208 ms / Memory 22.5 MB
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if node is None:
                return 0
            
            print(node.val)
            
            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            else:
                return dfs(node.left) + dfs(node.right) + node.val
        
        return dfs(root)
```

   

## 53. 이진 탐색 트리(BST) 노드 간 최소 거리

- https://leetcode.com/problems/minimum-distance-between-bst-nodes/

>**783. Minimum Distance Between BST Nodes** (Easy)
>
>Given the `root` of a Binary Search Tree (BST), return *the minimum difference between the values of any two different nodes in the tree*.
>
>**Note:** This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
>
> 
>
>**Example 1:**
>
>![img](https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg)
>
>```
>Input: root = [4,2,6,1,3]
>Output: 1
>```
>
>**Example 2:**
>
>![img](https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg)
>
>```
>Input: root = [1,0,48,null,null,12,49]
>Output: 1
>```
>
> 
>
>**Constraints:**
>
>- The number of nodes in the tree is in the range `[2, 100]`.
>- `0 <= Node.val <= 105`

  

### 1)  재귀 구조로 중위 순회

- 값의 차이가 가장 작은 노드를 찾으려면 어디와 어디 노드를 비교해야할까?
-  BST의 왼쪽 자식은 항상 루트보다 작고, 오른쪽 자식은 항상 루트보다 크다.
- **중위 순회** 를 하면서 이진 탐색 값과 현재 값을 비교

```python
# Runtime 36 ms / Memory 14.3 MB
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize
    
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val
        
        if root.right:
            self.minDiffInBST(root.right)
            
        return self.result
```



### 2)  재귀 구조로 중위 순회

- 동일한 알고리즘을 반복 구조로 구현
- 반복 구조에서는 `prev`, `result` 를 한 함수 내에서 처리하여 함수 내 변수로 선언

```python
# Runtime 44 ms / Memory 14.3 MB
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        prev = -sys.maxsize
        result = sys.maxsize
        
        stack = []
        node = root
        
        # 반복 구조 중위 순회 비교 결과
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
                
            node = stack.pop()
            
            result = min(result, node.val - prev)
            prev = node.val
        
            node = node.right
            
        return result
```

