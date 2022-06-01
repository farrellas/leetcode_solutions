def frog_problem(n):
    if n >= 2:
        return frog_problem(n-1) + frog_problem(n-2)
    else:
        return 1

# print(frog_problem(11))


def frog_bottom_up(n):
    first = 1
    second = 1
    output = 0
    if n < 2:
        return 1

    for i in range(2, n+1):
        output = first + second
        first = second
        second = output
        
    return output

print(frog_bottom_up(11))


def frog_bottom_up_w_x(n, x):
    if n == 0:
        return 1
    lst = [1]
    for i in range(1, n+1):
        total = 0
        for j in x:
            if i-j >= 0:
                total += lst[i-j]
        lst[i] = total
    return lst[n]