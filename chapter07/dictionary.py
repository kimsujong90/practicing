x = {"a":[1,2,3], "b":2, "c":3}

for k in x:
    print(k)

for i in x.values():
    print(i)

for k in x.keys():
    print("{}:{}".format(k, x[k]))

for t in x.items():
    print("{}:{}".format(t[0], t[1]))

