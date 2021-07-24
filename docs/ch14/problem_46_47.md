## 46. 두 이진 트리 병합

- https://leetcode.com/problems/merge-two-binary-trees/

>**617. Merge Two Binary Trees** (Easy)
>
>You are given two binary trees `root1` and `root2`.
>
>Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
>
>Return *the merged tree*.
>
>**Note:** The merging process must start from the root nodes of both trees.
>
> 
>
>**Example 1:**
>
>![img](https://assets.leetcode.com/uploads/2021/02/05/merge.jpg)
>
>```
>Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
>Output: [3,4,5,5,4,null,7]
>```
>
>**Example 2:**
>
>```
>Input: root1 = [1], root2 = [1,2]
>Output: [2,2]
>```
>
> 
>
>**Constraints:**
>
>- The number of nodes in both trees is in the range `[0, 2000]`.
>- `-104 <= Node.val <= 104`

### 1) 재귀 탐색

- 각각 이진트리의 루트부터 시작해 합쳐 나가면서 좌, 우 자식노드 또한 병합될 수 있도록 각 트리 자식 노드를 재귀호출한다.

- 만약, 어느 한 쪽에 노드가 존재하지 않는다면 존재하는 노드만 리턴하고 재귀호출 중단

  - 양쪽 노드가 모두 존재하지 않으면 None이 리턴

  ```python
  def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
      if t1 and t2:
          ...
      else:
          return t1 or t2
  ```

- 후위 순위 (Post-Order) - 리턴 순서 기준

  - 왼쪽 노드의 자식  -> 왼쪽 노트 -> 오른쪽 노드의 자식  -> 오른쪽 노드 -> 부모노드
  - 가장 밑단인 1번부터 리턴 값을 차례대로 받아오며, 9번에서 모든 리턴이 마무리되고 병합된 최종 결과가 남게 됨

  ![image](https://user-images.githubusercontent.com/19264527/111891483-c69d5980-8a36-11eb-9391-c87e56514a9c.png)

  

#### 내 풀이

```python
# Runtime 92 ms / Memory 15.5 MB
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
            return root1
        elif root2:
            return root2
        elif root1:
            return root1
```

  

#### 전체 풀이

```python
# Runtime 92 ms / Memory 15.4 MB
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            
            return node
        else:
            return t1 or t2
```

   

## 47. 이진트리의 직렬화 & 역직렬화

- https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

>**297. Serialize and Deserialize Binary Tree** (Medium)
>
>Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
>
>Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
>
>**Clarification:** The input/output format is the same as [how LeetCode serializes a binary tree](https://leetcode.com/faq/#binary-tree). You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
>
> 
>
>**Example 1:**
>
>![img](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)
>
>```
>Input: root = [1,2,3,null,null,4,5]
>Output: [1,2,3,null,null,4,5]
>```
>
>**Example 2:**
>
>```
>Input: root = []
>Output: []
>```
>
>**Example 3:**
>
>```
>Input: root = [1]
>Output: [1]
>```
>
>**Example 4:**
>
>```
>Input: root = [1,2]
>Output: [1,2]
>```
>
> 
>
>**Constraints:**
>
>- The number of nodes in the tree is in the range `[0, 104]`.
>- `-1000 <= Node.val <= 1000`

  

### 1)  직렬화 & 역직렬화 구현

- 직렬화(Serialize) : '이진 트리'와 같은 **논리적 구조**를 파일이나 디스크에 저장하기 위해 **물리적인 형태**로 바꿔주는 것. 반대는 **역직렬화(Deserialize)**
- `pickle` - 파이썬 직렬화 모듈
  - 피클링(Pickling) - 파이썬 객체의 계층 구조를 바이트 스트림으로 변경하는 작업



### 직렬화

- 이 문제는 직렬화 알고리즘에 대한 제약이 없음. (BFS, DFS 상관 없이 구현 가능)

- 이진트리를 BFS로 표현하면 순서대로 배치되기 때문에, DFS에 비해 매우 직관적

  ![image](https://user-images.githubusercontent.com/19264527/111892953-f7838b80-8a42-11eb-9cb4-fb12d161ef39.png)

-  BFS 반복 풀이 이용 (45번 이진 트리 반전 문제)

  - 문자열을 리턴
  - 불필요한 스왑 부분 제거

  ```python
  def serialize(self, root: TreeNode) -> str:
      queue = collections.deque([root])
      result = ['#']
      
      while queue:
          node = queue.popleft()
          if node:
              queue.append(node.left)
              queue.append(node.right)
          ...
     return result
  ```

- `result` 변수를 처리할 비즈니스 로직 구현

  - `result` 에는 현재 노드의 값을 추가
  - 큐에 BFS 탐색 결과가 계속 추가되면서 마지막 노드까지 차례대로 배열로 표현
  - 노드가 존재하지 않을 경우 널이라는 의미로 `#` 추가

  ```python
  def serialize(self, root):
      ...
      while queue:
          node = queue.popleft()
          if node:
              queue.append(node.left)
              queue.append(node.right)
                  
              result.append(str(node.val))
          else:
              result.append('#')
     return ' '.join(result)
  ```

- `result` 는 문자열로 바꿔줌

  ```python
  return ' '.join(result)
  ```

- 예제 입력값 기준 직렬화 결과 - `# A B C # # D E # # # #`

  - D, E 의 왼쪽, 오른쪽 자식이 없어서 #이 붙음

  

### 역직렬화

- 큐를 이용하여 역직렬화

- 문자열 형태의 입력값 처리

  - `split()` 으로 공백 단위로 문자열을 끊어서 `nodes`라는 리스트 변수를 만든다.
  - 트리로 만들어줄 노드 변수 root부터 셋팅하고 큐 변수 생성

  ```python
  def deserialize(self, data: str) -> TreeNode:
      nodes = data.split()
          
      root = TreeNode(int(nodes[1]))
      queue = collections.deque([root])
      ...
  ```

- 큐를 순회하면서 처리

  - 왼쪽 자식과 오른쪽 자식은 각각 별도의 인덱스를 부여받아 다음과 같이 `nodes` 를 탐색해 나감. (마치 런너 기법에서 **빠른 런너**가 먼저 노드를 탐색해나가는 것과 유사)
    - ![image](https://user-images.githubusercontent.com/19264527/111892631-7a571700-8a40-11eb-8cdb-ab422a4ee3e5.png)
  - `#`인 경우에는 큐에 삽입하지 않고, 아무런 처리도 하지 않는다.
  - ex. `# A B C # # D E # # # #`
    - `E` 이후에 더 이상 큐에 삽입되지 않음
    - 빠른 런너처럼 훨씬 더 앞의 `#` 은 읽어들이긴 하지만  `#` 이므로 아무런 처리도 하지 않는다.
    - 끝까지 순회하고 나면 원래의 트리구조로 복원

  ```python
  def deserialize(self, data):
      ...
      index = 2
      while queue:
          node = queue.popleft()
          if nodes[index] is not '#':
              node.left = TreeNode(int(nodes[index]))
              queue.append(node.left)
          index += 1
              
          if nodes[index] is not '#':
              node.right = TreeNode(int(nodes[index]))
              queue.append(node.right)
          index += 1
      ...
  ```

  

#### 전체 풀이

```python
# Runtime 248 ms / Memory 18.9 MB
class Codec:

    def serialize(self, root):
        queue = collections.deque([root])
        result = ['#']
        # 트리 BFS 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                
                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)
        

    def deserialize(self, data):
        # 예외 처리
        if data =='# #':
            return None
        
        nodes = data.split()
        
        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        
        # 빠른 런너처럼 자식노드의 결과를 먼저 확인 후 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            
            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root
```