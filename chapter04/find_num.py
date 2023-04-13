import random as r
r_num = r.randint(1,100)

num = int(input("숫자를 맞혀 보세요. (1 ~ 100),\n"))
while num != r_num:
    if num > r_num:
        print("숫자가 너무 커요")
    else:
        print("숫자가 너무 작아요")
        num = int(input())
print("정답입니다.")

