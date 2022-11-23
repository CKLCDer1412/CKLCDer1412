def minPathsum(grid):
    def minPath(i, j):
        if i > ncols or j > nrows:
            return float("inf")
        if i == ncols and j == nrows:
            return grid[j][i]
        if i not in res and j not in res:
            res[i, j] = grid[j][i] + min(minPath(i+1, j),minPath(i, j+1))
        return res[i, j]
    res, ncols, nrows = {}, len(grid[0])-1, len(grid)-1
    return minPath(0,0)

grid=[[1,2,1],
      [1,5,2],
      [2,3,1]]
print(minPathsum(grid))