# 14장 트리

### 44 가장 긴 동일 값의 경로
> 동일한 값을 지닌 가장 긴 경로를 찾아라

![ex1](https://user-images.githubusercontent.com/30167661/111902294-3257e480-8a80-11eb-9504-9627dcb2ec3c.jpg)

```
Input: root = [5,4,5,1,1,5]
Output: 2
```

![ex2](https://user-images.githubusercontent.com/30167661/111902300-3edc3d00-8a80-11eb-9a3f-2ae01d0b1d7b.jpg)

``` 
Input: root = [1,4,5,4,4,5]
Output: 2
```

#### 내 풀이

```python3
class Solution:
    sol = 0
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(root: TreeNode):
            
            # 초기 null 값 체크
            if root is None:
                return 0
            
            # 왼쪽, 오른쪽 DFS
            left_val = dfs(root.left)
            right_val = dfs(root.right)
            
            # 왼쪽 노드가 있고 왼쪽 노드와 지금이 같다면 +1 아니면 0
            if root.left and root.left.val == root.val:
                left_val += 1
            else:
                left_val = 0
            
            # 오른쪽 노드가 있고 오른쪽 노드와 같다면 +1 아니면 0
            if root.right and root.right.val == root.val:   
                right_val += 1
            else:
                right_val = 0
            
            # 최대값을 구해서 sol 업데이트
            self.sol = max(self.sol, left_val+right_val)
            
            # 자식 노드 상태값 중 큰 값 다시 리턴
            return max(left_val, right_val)

        dfs(root)
        return self.sol
```

### 45 이진 트리 반전
> 중앙을 기준으로 이진 트리를 반전시키는 문제

![invert1-tree](https://user-images.githubusercontent.com/30167661/111902308-4c91c280-8a80-11eb-9e3f-0f35b2a251e2.jpg)

```
nput: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

![invert2-tree](https://user-images.githubusercontent.com/30167661/111902316-5adfde80-8a80-11eb-8441-9e8a64f0775d.jpg)

``` 
Input: root = [2,1,3]
Output: [2,3,1]
```

``` 
Input: root = []
Output: []
```

#### 내 풀이

```python3
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            
            if not root:
                return None
            
            root.left, root.right = root.right, root.left
            
            if root.left:
                dfs(root.left)
                
            if root.right:
                dfs(root.right)
            
        dfs(root)
        return root
```

### 책 풀이
#### 기본 풀이
```python3
def inverTree(self, root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = self.inverTree(root.right), self.inverTree(root.left)
    
    # 파이썬에서는 return 값이 없으면 자동으로 None을 리턴 한다.
    return root
```

#### BFS 풀이
```python3
def invertTree(self, root: TreeNode) -> TreeNode:
    queue = collections.deque([root])
    
    while queue:
        node = queue.popleft()
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)    

    return root
```

#### DFS 풀이
```python3
def invertTree(self, root: TreeNode) -> TreeNode:
    queue = collections.deque([root])
    
    while queue:
        node = queue.popleft()
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)    

    return root
```

#### 전위, 후위 풀이
```python3
def invertTree(self, root: TreeNode) -> TreeNode:
    stack = collections.deque([root])
    
    while stack:
        node = stack.popleft()
        # 부모 노드부터 하향식 스왑
        if node:
            # 전위 순위
            # node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)
            
            # 후위 순위
            node.left, node.right = node.right, node.left    

    return root
```
