def func(x):
    return (x * x * x) + x - 1


def bisection(m, n):
    if (func(m) * func(n)) >= 0:
        return
    while abs(n - m) >= 0.0001:
        x0 = (m + n) / 2
        if func(x0) == 0.0:
            break
        if (func(m) * func(x0)) < 0:
            n = x0
        else:
            m = x0
    print("root exist in : ", "%.8f" % x0)


a = 0.6
b = 0.8
bisection(a, b)