def test(**kwargs):
    print(kwargs)
    for x in kwargs:
        print(x)
    for x in kwargs.items():
        print(x)
    for k, v in kwargs.items():
        print(k, v)

test(a=1, b=2, c=3)

