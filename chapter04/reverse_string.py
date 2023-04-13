my_string = input("문자열을 입력하세요 : ")
str_cnt = len(my_string)

result = []
for i in range(str_cnt):
    result += my_string[i]

print(result)
print(result[::-1])