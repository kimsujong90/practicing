def f(x):
    y = x
    x = 5
    return y * y

x = 3
ret_val = f(x)
print(ret_val)
print(x)

