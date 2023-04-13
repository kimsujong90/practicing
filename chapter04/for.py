data = [1,2,3,4,5]

for _ in data:
    print("hello")

for v in data:
    print(v)

for (idx, v) in enumerate(data, start=1):
    print("[",idx, "] : ", v)

for v in enumerate(data):
    print(v[0])

for looper in range(2,20,2):
    print(looper)

