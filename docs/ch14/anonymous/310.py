# https://leetcode.com/problems/minimum-height-trees/
from typing import *
import collections
import time


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for node_from, node_to in edges:
            # undirected로 양방향 가능
            graph[node_from].append(node_to)
            graph[node_to].append(node_from)

        # 리프 노드를 담는다
        leaves = []
        for i in range(n + 1):
            # 리프 노드는 연결된 노드가 하나밖에 없다
            if len(graph[i]) == 1:
                leaves.append(i)
        # 루트가 남을 때까지 반복
        while n > 2: # 왜 2인가? 하나만 남거나, 서로 연결된 두 노드만 남거나 둘 중 하나
            '''
            n은 존재하는 노드의 수. 연결된 노드의 개수를 지워나가다 보면 루트 노드 개수만 남게 되는데, 루트 노드가 1개 또는 2개 존재 가능하다
            [[8,7],[7,6],[6,5],[6,4],[6,3],[3,2],[3,1],[1,0]]
            8   5   2
            |   |   |
            7---6---3---1---0
                |
                4
            
            3개 이상은 불가능할까? 3개가 되면 6, 3, 1 남고, 6과 1이 제거되면서 3만 루트 노드가 된다
            8   5   2   ?
            |   |   |   |
            7---6---3---1---0
                |
                4
            '''
            n -= len(leaves)
            leaves_new = []
            # 리프 노드와 연결된 노드를 서로 지운다(p.311 섬의 개수 문제와 유사하다)
            for leaf in leaves:
                # print('leaf: ', leaf, ', graph: ', graph)
                # 리프노드와 연결된 neigbor를 꺼내서
                neighbor = graph[leaf].pop()
                # 리프 노드를 제거한다
                graph[neighbor].remove(leaf)
                # print('neighbor: ', neighbor, ', graph: ', graph)

                # 연결된 노드가 하나만 있는 새로운 리프 노드가 있다면, 계속 지워나가도록 leaves를 바꾼다
                if len(graph[neighbor]) == 1:
                    leaves_new.append(neighbor)

            leaves = leaves_new
            # print()
        
        return leaves

    def first(self, n: int, edges: List[List[int]]) -> List[int]:
        # Wrong Answer
        if n == 1:
            return [0]

        adjacent_list = collections.defaultdict(list)

        for edge in edges:
            adjacent_list[edge[0]].append(edge)
            adjacent_list[edge[1]].append([edge[1], edge[0]])

        possbile_roots = [*adjacent_list]
        """ print(adjacent_list)
        print(possbile_roots) """

        def dfs(root, neighbor, path, depth):
            if root == neighbor:
                return depth - 1

            depth_max = depth  
            # print('root:', root, ', neighbor:', neighbor, ', path:', path)
            for node in adjacent_list[neighbor]:
                if node[1] not in path:
                    depth_new = dfs(root, node[1], path + [node[1]], depth + 1)
                    depth_max = max(depth_max, depth_new)
                    # print('depth_new:', depth_new, ', depth_max:', depth_max)
            
            return depth_max

        depth_dict = collections.defaultdict(list)
        depth_min = 20001
        while possbile_roots:
            depth_max = 0
            root = possbile_roots.pop(0)

            for node in adjacent_list[root]:
                depth_max = max(depth_max, dfs(root, node[1], [node[1]], 1))
            
            if root not in depth_dict[depth_max]:
                depth_min = min(depth_max, depth_min)
            depth_dict[depth_max].append(root)

        """ print(depth_min)
        print(depth_dict) """

        return depth_dict[depth_min]