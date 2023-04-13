my_list = [10,20,30,40,50,60,70,80]

print(my_list[1:5]) # [1] ~ [4]
print(my_list[1:]) # [1] ~ [7]
print(my_list[:]) # [0] ~ [7]

print(my_list[-7:-3]) # [1] ~ [4]
print(my_list[-1]) # 마지막 원소
print(my_list[-3:]) # 마지막 원소 3개를 읽어오는 slicing

print(my_list[1:8:-1]) # 에러 테스트
print(my_list[::2]) # [0],[2],[4],[6]

my_list2 = my_list + my_list
print(my_list2)

my_list3 = my_list * 2
print(my_list3)

print(50 in my_list)
print(90 in my_list)

