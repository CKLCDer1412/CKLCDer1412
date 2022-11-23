def changeATM(amount, coins):
    def ways(amount, coins, n):
        if amount == 0:
            return 1
        elif amount < 0 or len(coins) == 0:
            return 0
        elif amount not in res and n not in res:
            res[(amount, n)]=ways(amount-coins[-1], coins, n) + ways(amount, coins[:-1], n-1)
        return res[(amount, n)]
    res= {}
    return ways(amount, coins, len(coins)-1)

amount=int(input())
coins=[int(i)for i in input().split()]
print(changeATM(amount, coins))
    