def minCost(n, cost, memo):
    if n < 2:
        return 0
    
    if n in memo:
        return memo[n]
    
    oneStep = minCost(n-1, cost, memo) + cost[n-1]
    twoStep = minCost(n-2, cost, memo) + cost[n-2]
    memo[n] = min(oneStep, twoStep)
    return memo[n]

def minCostClimbingStairs(cost):
    memo = {}

    return minCost(len(cost) - 1, cost, memo)
