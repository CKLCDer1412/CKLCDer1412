def uniquePath(obs):
    def ways(i , j):
        if i == cols and j == rows and obs[j][i] == 0:
            return 1
        if i > cols or j > rows or  obs[j][i] == 1:
            return 0
        if i not in res and j not in res:
            res[i, j] = ways(i+1, j) + ways(i, j+1)
        return res[i, j]
    res={}
    cols, rows = len(obs[0])-1, len(obs)-1
    return ways(0, 0)

obs = [[0,0,0],
                [0,0,0],
                [0,0,0]]
print(uniquePath(obs))