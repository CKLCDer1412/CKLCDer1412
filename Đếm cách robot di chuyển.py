def uniquePathWith0bstacles(obstacleGrid):
    def ways(i , j):
        if i == cols and j == rows and obstacleGrid[j][i] == 0:
            return 1
        if i > cols or j > rows or  obstacleGrid[j][i] == 1:
            return 0
        if i not in res and j not in res:
            res[i, j] = ways(i+1, j) + ways(i, j+1)
        return res[i, j]
    res={}
    cols, rows = len(obstacleGrid[0])-1, len(obstacleGrid)-1
    return ways(0, 0)

obstacleGrid = [[0,0,0],
                [0,0,0],
                [0,0,0]]
print(uniquePathWith0bstacles(obstacleGrid))