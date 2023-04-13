f = open(r"C:\Users\d\Desktop\Naver MYBOX\메디치 빅데이터 4기\파이썬\pythonProject\chapter06\yesterday.txt",'r')
yesterday_lyric = f.readlines()
f.close()

contents = ""
for line in yesterday_lyric:
    contents = contents + line.strip() + "\n"

c_yesterday = contents.upper().count("YESTERDAY")
print("몇개인가: ", c_yesterday)