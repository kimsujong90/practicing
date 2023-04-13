std_score = int(input("성적을 입력하세요 : "))

if std_score > 89:
    grade = 'A'
elif std_score > 79:
    grade = 'B'
elif std_score > 69:
    grade = 'C'
elif std_score > 59:
    grade = 'D'
else:
    grade = 'F'

print(grade)


