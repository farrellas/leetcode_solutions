def climbStairs(n):
    if n <= 3:
        return n
    first = 2
    second = 3
    output = 0
    for i in range(4, n+1):
        output = first + second
        first = second
        second = output
    
    return output