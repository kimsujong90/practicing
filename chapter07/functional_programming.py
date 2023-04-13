import random

random.seed(123)

data = random.choices(range(1,21), k=8)
print(data)

sorted_data = sorted(data, reverse=True)
print(sorted_data)

from collections import OrderedDict

dict1 = {
    "a": 10,
    "c": 25,
    "b": 4
}

print(dict1)

def by_key(t):
    return t[0]

def by_value(t):
    return t[1]

print(sorted(dict1.items(), key=by_key))
print(sorted(dict1.items(), key=by_value))

o_dict1 = OrderedDict(sorted(dict1.items(), key=by_key))
print(o_dict1)

for k, v in o_dict1.items():
    print(f"{k}:{v}")

score = [90, 80, 70, 60]

new_score = [v+5 for v in score]
print(new_score)

new_score = []
for v in score:
    new_score.append(v+5)
print(new_score)

new_score = []
def up_5(x):
    return x + 5

for v in map(up_5,score):
    new_score.append(v)
print(new_score)

new_score = []
new_score = list(map(lambda x: x+5, score))
print(new_score)

d = dict()
print(d.get("first"))