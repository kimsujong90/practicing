kor_score = [49,80,20,100,80]
math_score = [43,60,85,30,90]
eng_score = [49,82,48,50,100]
midterm_score = [kor_score,math_score,eng_score]

student_score = [0,0,0,0,0]
f = len(midterm_score)
i = 0

for subject_score in midterm_score:
    for score in subject_score:
        student_score[i] += score
        i += 1
        print(student_score)
    i = 0
    a,b,c,d,e = student_score
    student_average = [a/f,b/f,c/f,d/f,e/f]
print(student_average)

for seq, total in enumerate(student_score, start=1):
    print(seq, total/f)
