def func(x):
    return x * x * x + x - 1


def derivfunc(x):
    return 3 * x * x + 1


def newton(x):
    h = func(x) / derivfunc(x)

    while abs(h) > 0.0001:
        h = func(x) / derivfunc(x)
        x = x - h
    print("root exist in : ", "%.8f" % x)


x0=2
newton(x0)