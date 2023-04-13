a = [4,5,2,1,3]
b = a

sorted_a = sorted(a)
print(sorted_a)
print(a)
print(b,'\n')

sorted_a = sorted(a, reverse=True)
a.sort()
print(sorted_a)
print(a)
print(b)
