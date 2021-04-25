from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        n = len(grid)
        if 0 == n:
            return 0
        m = len(grid[0])

        def DFS(grid, i, j):
            if i < 0 or j < 0 or i >= n or j >= m or "1" != grid[i][j]:
                return
            grid[i][j] = "0"
            DFS(grid, i + 1, j)
            DFS(grid, i - 1, j)
            DFS(grid, i, j + 1)
            DFS(grid, i, j - 1)

        for i in range(n):
            for j in range(m):
                if "1" == grid[i][j]:
                    DFS(grid, i, j)
                    cnt += 1
        return cnt


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    # grid = [
    #     ["1", "1", "0", "0", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "1", "0", "0"],
    #     ["0", "0", "0", "1", "1"]
    # ]
    obj = Solution()
    print(obj.numIslands(grid))
