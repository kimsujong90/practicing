std_age = int(input("당신이 태어난 연도를 입력하세요 : "))
age = 2020 - (std_age+1)

if age > 26:
    status = '학생이 아닙니다.'
elif age > 19:
    status = '대학생'
elif age > 16:
    status = '고등학생'
elif age > 13:
    status = '중학생'
elif age > 7:
    status = '초등학생'
else :
    status = '학생이 아닙니다'

print(status)
