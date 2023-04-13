data = "10, 20, 30, 40, 50"
data_list = []

data = data.replace(" ","").split(",")

for v in data:
    if v.isdigit():
        data_list.append(int(v))
    else:
        print("[{}]:{}은 숫자포맷이 아닙니다.".format(i, v))

print(data_list)