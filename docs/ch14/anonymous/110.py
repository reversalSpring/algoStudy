# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(node: TreeNode, depth):
            if not node.right and not node.left:
                return depth
            
            dfs_left = depth
            dfs_right = depth
            if node.left:
                dfs_left = dfs(node.left, depth + 1)
            if node.right:
                dfs_right = dfs(node.right, depth + 1)

            # print('dfs_left: ', dfs_left, ', dfs_right', dfs_right)
            if dfs_left is False or dfs_right is False:
                return False
            
            if abs(dfs_left - dfs_right) <= 1:
                return max(dfs_left, dfs_right)
            else:
                return False

        if dfs(root, 1) is False:
            return False
        else:
            return True
    

    def solution_by_book(self, root: TreeNode) -> bool:
        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)
            # 높이 차이가 나는 경우 -1, 이 외에는 높이에 따라 1 증가
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1
        
        return check(root) != -1


    def second(self, root: TreeNode) -> bool:
        if not root:
            return True

        if not root.val:
            return True

        def bfs(node: TreeNode):
            res = []
            if not node:
                return res

            queue = [node]
            res.append(node.val)
            while queue:
                node_curr = queue.pop(0)

                if not node_curr.left and not node_curr.right:
                    continue

                if node_curr.left:
                    res.append(node_curr.left.val)
                    queue.append(node_curr.left)
                else:
                    res.append(None)

                if node_curr.right:
                    res.append(node_curr.right.val)
                    queue.append(node_curr.right)
                else:
                    res.append(None)
                    
            return res
        
        list_left = bfs(root.left)
        list_right = bfs(root.right)
        print(list_left)
        print(list_right)

            

    def first(self, root: TreeNode) -> bool:
        if not root:
            return True
        # AttributeError: 'NoneType' object has no attribute 'val'
        if not root.val:
            return True

        def dfs(node: TreeNode, depth):
            if not node:
                return depth - 1

            return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))

        return abs(dfs(root.left, 1) - dfs(root.right, 1)) <= 1

s = Solution()

print(s.solution_by_book(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))))
print(s.solution_by_book(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
print(s.isBalanced(TreeNode()))
print(s.isBalanced(TreeNode(1)))
print(s.isBalanced(TreeNode(1, TreeNode(2))))
print(s.isBalanced(TreeNode(1, TreeNode(2, TreeNode(3)))))
# [1,2,2,3,null,null,3,4,null,null,4]
'''
          1
       2     2
    3           3 
 4                 4
'''
case3 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), None)), TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
print(s.isBalanced(case3))

