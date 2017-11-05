class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cur_max_island = 0
        for irow, row in enumerate(grid):
            for icol, col in enumerate(row):
                if grid[irow][icol] == 1:
                    cur_max_island = max(cur_max_island, self.find_island_size(irow, icol, grid, 1))
        return cur_max_island

    def find_island_size(self, y, x, array, count):
        array[y][x] = 0
        if y > 0:
            if array[y - 1][x] == 1:
                count = self.find_island_size(y - 1, x, array, count + 1)
        if y < len(array) - 1:
            if array[y + 1][x] == 1:
                count = self.find_island_size(y + 1, x, array, count + 1)
        if x > 0:
            if array[y][x - 1] == 1:
                count = self.find_island_size(y, x - 1, array, count + 1)
        if x < len(array[0]) - 1:
            if array[y][x + 1] == 1:
                count = self.find_island_size(y, x + 1, array, count + 1)
        return count


array = [[0,1],[1,1]]

print(Solution().maxAreaOfIsland(array))
