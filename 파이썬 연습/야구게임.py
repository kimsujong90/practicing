import random as r

while True:
    number = str(r.randint(000,999))
    if len(set(number))==3:
        break
    
attempt=0
while True:
    try:
        ans=str(input('세자리 숫자를 입력해 주세요 : '))
        if len(ans) != 3:
            print('세자리 숫자가 아닙니다.')
            continue
    except:
        print('올바른 형태를 입력해주세요')
        continue

    attempt+=1
    strike=0
    ball=0
    for i in range(2):
        if ans[i]==number[i]:
            strike+=1
        if ans[i]==number[(i+1)%3] or ans[i]==number[(i+2)%3]:
            ball+=1
    if strike == 0 and ball == 0:
        print("아웃입니다!")
    elif strike == 3:
        print('정답입니다! 총 시도 횟수는 %d회 입니다'%attempt)
        break
    else:
        print('%d 스트라이크 %d볼 입니다.'%(strike,ball))
        
