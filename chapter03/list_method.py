color = ['red','green','blue']
color2 = ['yellow','purple']

color.append('white')
color.extend(color2)
color.extend("silver")
print(color)

color.insert(2,'orange')
print(color)
print(color.pop(3))

color.insert(3,'black')
print(color)

color.remove('black')
print(color)

del color[3]
print(color)

idx = color.index('purple')
color[idx] = 'bronze'
print(color)

my_list = [10,20,30,10,15,10]

first_idx = my_list.index(10)
print(my_list.index(10, first_idx + 1))

silver_index = color.index('s')
del color[silver_index:]
print(color)

print(sum(my_list)/len(my_list))
