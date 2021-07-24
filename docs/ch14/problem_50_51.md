# 14장 트리
## <a name='TOC'>목차</a>
0. [목차](#TOC)
1. [이진 탐색 트리(Binary Search Tree](#0)
2. [정렬된 배열의 이진 탐색 트리 변환(Convert Sorted Array to Binary Search Tree)](#1)
3. [이진 탐색 트리를 더 큰 수 합계 트리로(Binary Search Tree to Greater Sum Tree)](#2)

## <a name='0'>이진 탐색 트리(Binary Search Tree)</a>
### (1) 이진 탐색 트리(BST)
- 생성
  ```python3
  class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
  def insert(root, key):
      if root is None:
          return Node(key)
      else:
          if root.val == key:
              return root
          elif root.val < key:
              root.right = insert(root.right, key)
          else:
              root.left = insert(root.left, key)
  ```
- 주어진 값 찾기
  ```python3
  def search(root,key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right,key)
    return search(root.left,key)
  ```
### (2) 자가 균형 이진 탐색 트리(Self-Balancing BST)
- **높이의 균형을 맞추는 작업은 성능 측면에서 매우 중요하다**
- **AVL Tree**
  - Adelson-Velskii / Landis에 의해 1962년 제안된 트리
  - 각 노드의 왼쪽 서브트리와 오른쪽 서브트리의 높이 차이가 1 이하인 BST
  - 탐색 시간: O(logn)
  - Red-Black Tree 보다는 효율이 떨어짐
  - [구현 예시](https://www.geeksforgeeks.org/avl-tree-set-1-insertion/?ref=rp)
- [**Red-Black Tree**](https://m.blog.naver.com/pqzmggg/90120883769)
  - ![image](https://user-images.githubusercontent.com/75566147/112739693-3ff5f880-8fb1-11eb-956e-60c1d5351cbf.png)
  - 모든 노드의 색상이 Red 또는 Black인 BST
    - 모든 노드는 Red 혹은 Black 중 하나이다.
    - 루트 노드는 Black이다.
    - 모든 말단 노드는 Black이다.
    - Red 노드의 자식 노드들은 언제나 Black이며, Black 노드만이 Red 노드의 부모가 될 수 있다.
    - 어떤 노드로부터 시작하여 말단 노드에 도달하는 모든 경로에는 (말단 노드를 제외하면) 모두 같은 개수의 Black 노드가 있다.
  - BST 중 가장 효율적
  - [구현 예시](https://www.geeksforgeeks.org/red-black-tree-set-1-introduction-2/)


## <a name='1'>[#108 - 정렬된 배열의 이진 탐색 트리 변환(Convert Sorted Array to Binary Search Tree)](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)</a>
### 문제
![image](https://user-images.githubusercontent.com/75566147/112739281-efc96700-8fad-11eb-98a1-b92742784545.png)
### (1) 내 풀이
```python3
class Solution:
    def insert(root, key):
        if root is None:
            return TreeNode(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = Solution.insert(root.right, key)
            else:
                root.left = Solution.insert(root.left, key)
        return root

    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        root = TreeNode()
        if len(nums) == 1:
            root.val = nums[0]
            return root
        
        med = len(nums)//2
        if med == 0:
            return
        
        left_nums = nums[:med]
        right_nums = nums[med+1:]
        root.val = nums[med]
        
        root.left = self.sortedArrayToBST(left_nums)
        root.right = self.sortedArrayToBST(right_nums)
        
        for num in left_nums:
            Solution.insert(root, num)
        
        for num in right_nums:
            Solution.insert(root, num)
            
        return root
```
- Point
  - BST 생성을 위한 코드 그대로 이식
  - 배열의 중앙값을 사용

### (2) 책 풀이 - 이진 검색 결과로 트리 구성
```python3
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    if not nums:
        return None
        
    mid = len(nums)//2
    
    # 분할 정복으로 이진 검색 결과 트리 구성
    node.left = self.sortedArrayToBST(nums[:mid])
    node.right = self.sortedArrayToBST(nums[mid+1:])
```
- Point
  - 좌/우 각각 중앙값을 기준으로 계속 절반씩 잘라서 재귀 호출을 한다.
  

## <a name='2'>[#1038 - 이진 탐색 트리를 더 큰 수 합계 트리로(Binary Search Tree to Greater Sum Tree)](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)</a>
### 문제
![image](https://user-images.githubusercontent.com/75566147/112739282-f1932a80-8fad-11eb-9604-5fbd951a85ad.png)
### (1) 내 풀이
```python3
class Solution:
    sum = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(curr):
            if curr:
                dfs(curr.right) # 이걸 빠져나왔다는 것은 끝에 도달했다는 의미
                # print(curr.val) 찍어보면 8-7-6-5-4-3-2-1-0
                self.sum += curr.val
                curr.val = self.sum
                dfs(curr.left)
                # print(curr.val) 찍어보면 8-15-26-21-33-35-36-36-30
            else:
                return
            
        dfs(root)
        return root
```
- Point
  - 계속 global하게 가져갈 합계 변수 필요 = sum
  - 끝까지 들어가서 시작한다 → DFS 사용함
  - 자기 자신을 기준으로, 오른쪽에 있는 모든 값들을 sum에 더하고, sum에 자신까지 더하여 만든 새로운 sum을 왼쪽으로 전달한다.

### (2) 책 풀이 - 중위 순회로 노드 값 추적
```python3
class Solution:
    val: int = 0
    
    def bstToGet(self, root: TreeNode) -> TreeNode:
        # 중위 순회 노드 값 누적
        if root:
            self.bstToGet(root.right)
            self.val += root.val  # 지금까지 누적된 값에 현재 노드의 값을 더한다.
            root.val = self.val
            self.bstToGst(root.left)
        return root
```
- Point
  - [중위 순회?](https://lgphone.tistory.com/93)
    - 깊이 우선 탐색의 세 가지 경우(전위, 후위, 중위) 중 하나
    - In-Order Traversal: 왼쪽 하위 트리를 방문 후 root를 방문 (왼쪽 자식 → 뿌리 → 오른쪽 자식)
    - ```python3
      def inorder(root):
          if root != 0:
              inorder(root.left)
              yield root.value
              inorder(root.right)
      ```

### (3) [타인의 풀이 - global 변수 사용 없이](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/discuss/286849/Easy-to-understand-Python-solution-beats-100-reversed-inorder)
```python3
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def recur(node, sumTillNow):
            if not node:
                return sumTillNow
            node.val += recur(node.right, sumTillNow)
            return recur(node.left, node.val)
        
        recur(root, 0)
        return root
```
