def pow(x, p):
    m = x
    t = 1
    while p:
        if p % 2:
            t *= m
        m *= m
        p //= 2
    return t

print(pow(5,2))