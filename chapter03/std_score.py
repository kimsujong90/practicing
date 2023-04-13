# 학생 4명의 국,영,수 점수
score_std = [
    [100, 95, 90, 95],
    [85, 85, 95, 85],
    [70, 85, 80, 65]
]

print("국어 점수 : ", score_std[0])
print("영어 점수 : ", score_std[1])
print("수학 점수 : ", score_std[2])

print("A학생의 국어점수 : ", score_std[0][0])
print("C학생의 영어점수 : ", score_std[1][2])

std = ['a','b','c','d']
num = [1,2,3,4]
std = num
print(std)

score_std = [
    [100, 95, 90, 95],
    [85, 85, 95, 85],
    [70, 85, 80, 65]
]

for i in range(len(score_std)): # 0 ~ 2
    for j in range(len(score_std[i])): # 0 ~ 3
        print(score_std[i][j], end=" ")
    print()

for i in range(len(score_std)):
    for j in range(len(score_std[i])):
        if j == 2:
            print(score_std[i][j], end=" ")
    print()

a = [1,2,3]
b = [4,5,6]

data = [a,b]
print(data)

a = 100
data = [a,b]
print(data)

b.sort()
print(b)

