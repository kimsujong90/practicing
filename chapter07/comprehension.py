key = ['a', 'b', 'c', 'd']
value = [1, 2, 3, 4]

dict1 = {k: v for k, v in zip(key, value)}
print(dict1)

dict2 = {}
for k,v in zip(key, value):
    dict2[k] = v
print(dict2)

dict3 = dict(zip(key, value))
print(dict3)
