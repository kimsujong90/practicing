for v in range(5):
    if v % 2 == 1:
        continue
    print(v)

while 1:
    q = input("Q를 입력하면 종료합니다.")
    if q == "Q" or "q":
        break
