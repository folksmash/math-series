def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    if n==0: return 2
    if n==1: return 1
    return lucas(n-1) + lucas(n-2)

# 4, 6, 10, 16, 26
def sum_series(n, start0=0, start1=1):
    if (start0 == 0 and start1 == 1): 
        return fibonacci(n)
    elif (start0 == 1 and start1 == 2): 
        return lucas(n)
    else:
        if n == 1: 
            return start0
        elif n == 2:
            return start1
        else:
            return (sum_series(n-1, start0, start1)) + (sum_series(n-2, start0, start1))
    # ret_val = start0
    # pacebehind = start1
    # for i in range(n):
    #     ret_val += pacebehind
    #     pacebehind = ret_val
