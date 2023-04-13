def f(x):
    x = 5
    y = x
    return y * y

x = 3

print(f(x))
print(x)

def spam(eggs):
    eggs.append(1)
    eggs = [2,3]

ham = [0]
spam(ham)
print(ham)

def test(t):
    x = t
    print(x)
    t = 20
    print(t)

x = 10
test(x)
print(x)

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(int(input("입력 : "))))
