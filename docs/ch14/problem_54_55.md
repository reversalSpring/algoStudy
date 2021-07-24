# 14장 트리

### 54 전위, 중위 순회 결과로 이진트리 구축

### 전위, 중위, 후위 순회

- 루트를 서브 트리에 앞서서 먼저 방문하면 전위 순회
- 루트를 왼쪽과 오른쪽 서브 트리 중간에 방문하면 중위 순회
- 루트를 서브 트리 방문 후에 방문하면 후위 순회가 된다.

![전중후](https://user-images.githubusercontent.com/30167661/113501727-6512da00-9562-11eb-959e-e4f5cfa93cfe.jpg)

## 책 풀이 (128 ms / 53 MB)
  
![전,중위 이진완성](https://user-images.githubusercontent.com/30167661/113506199-533f3000-957e-11eb-8c9d-275bfcd6da7e.jpg)


  ```python3
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index+1:])

            return node
  ```
  


## Discuss 풀이 (56 ms / 18.4 MB)
```python3
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        queue=collections.deque(preorder)
        inorder_lookup = {n: i for i, n in enumerate(inorder)}
        return self.dfs(queue, inorder_lookup, 0, len(inorder)-1)
        
    def dfs(self, queue, inorder_lookup, left, right):
        if left<=right:
            root = TreeNode(queue.popleft())
            ind = inorder_lookup[root.val]
            root.left = self.dfs(queue, inorder_lookup, left, ind-1)
            root.right = self.dfs(queue, inorder_lookup, ind+1, right)
            return root
```

### 55 배열의 K 번째 큰 요소
## 힙
- 우선순위 큐 --> 힙 --> 배열(보통 index 1부터 사용)
- 정렬되지 않음
 
- 힙 삽입 
1. 삽입하고자 하는 값을 트리의 가장 마지막 원소에 추가한다.
2. 부모노드와의 대소관계를 비교하면서 만족할 때까지 자리 교환을 반복한다.
![힙 삽입](https://user-images.githubusercontent.com/30167661/113506111-ca27f900-957d-11eb-95e7-53a922556daf.jpg)

- 힙 추출
1. 힙에서는 루트 노드만 삭제가 가능하므로 루트 노드를 제거한다.
2. 가장 마지막 노드를 루트로 이동시킨다.
3. 자식노드와 비교하여 조건이 만족할 때까지 이동시킨다.
- ![힙 추출](https://user-images.githubusercontent.com/30167661/113506126-e9bf2180-957d-11eb-903c-8aaf03dd428b.jpg)


## 힙 vs 이진 탐색 트리
- 상/하 VS 좌/우
- 최대/소 값 추출( O(1) ) VS 탐색/삽입 ( O(log n) )

## 풀이
```python3
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums:
            heapq.heappush(heap, (-num, num))
            // heapq.heappush(heap, -n)
        
        kth_min = None
        for _ in range(k):
            kth_min = heapq.heappop(heap)
        return kth_min[1]
        // return -heapq.heappop(heap)
```

## heapify 풀이
```python3
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)
```

## nlargest 풀이 (nsmallest 도 있음)
```python3
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
```

## 정렬 풀이
```python3
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
```

| 풀이 | 방식                             | 실행 시간 |
| ---- | -------------------------------- | --------- |
| 1    | heapq 모듈 이용                  | 72ms     |
| 2    | heapq 모듈의 heapify 이용        | 64ms     |
| 3    | heapq 모듈의 nlargest 이용       | 68ms     |
| 4    | 정렬을 이용한 풀이               | 56ms     |

