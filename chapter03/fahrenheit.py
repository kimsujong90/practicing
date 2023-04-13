print("본 프로그램은 섭씨온도를 화씨온도로 변환하는 프로그램입니다.")
celsius = input("변환하고 싶은 섭씨온도를 입력하세요. \n")
fahrenheit = (float(celsius) * 1.8) + 32

print("섭씨온도 : ", celsius)
print("화씨온도: ", round(fahrenheit,2))