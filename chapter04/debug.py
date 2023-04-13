import random

random.seed(11)
data = random.sample(range(1,46),6)

print(data)
result = []

for v in data:
    if v % 2 == 1:
        result.append(v)

print(result)
