import copy

'''
Runtime: 76 ms, faster than 12.00% of Python3 online submissions for Rotting Oranges.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Rotting Oranges.
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        row = len(grid)
        col = len(grid[0])
        while True:
            # keep changed grid in grid_at_t
            grid_at_t = copy.deepcopy(grid)
            for i in range(row):
                for j in range(col):
                    if grid[i][j] == 2:
                        if i - 1 >= 0 and grid[i-1][j] == 1:
                            grid_at_t[i-1][j] = 2
                        if i + 1 < row and grid[i+1][j] == 1:
                            grid_at_t[i+1][j] = 2
                        if j - 1 >= 0 and grid[i][j-1] == 1:
                            grid_at_t[i][j-1] = 2
                        if j + 1 < col and grid[i][j+1] == 1:
                            grid_at_t[i][j+1] = 2

            if grid == grid_at_t:
                break
            else:
                time += 1
                grid = grid_at_t
                            
        curr = set([e for row in grid for e in row]) 

        if 1 not in curr:
            return time
        else:
            return -1
