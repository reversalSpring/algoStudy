# https://leetcode.com/problems/number-of-islands/

from typing import *

'''
m x n 그리드
m == grid.length: 높이
n == grid[i].length: 너비

1: 섬
0: 물
섬의 개수를 구하라
'''

class Solution:
    grid: List[List[str]]

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        ans = 0
        count = 0
        if not self.grid:
            return ans
        
        for i in range(len(self.grid)):  # i = m = 높이
            for j in range(len(self.grid[0])): # j = n = 너비
                if self.grid[i][j] == '1':
                    self.dfs(i, j)
                    count += 1
        return count
    
    def dfs(self, i, j):
        '''
        i < 0 or i >= len(self.grid): 높이가 음수 또는 지도의 높이 초과
        j < 0 or j >= len(self.grid[0]): 너비가 음수 또는 지도의 너비 초과
        self.grid[i][j] != '1': 땅이 아닌 경우
        '''
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]) or self.grid[i][j] != '1':
            return
        
        # 육지를 지워나간다
        self.grid[i][j] = '0'
        self.dfs(i + 1, j)
        self.dfs(i - 1, j)
        self.dfs(i, j + 1)
        self.dfs(i, j - 1)


s = Solution()

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(s.numIslands(grid1))

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(s.numIslands(grid2))
