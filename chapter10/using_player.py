import player2

son = player2.SoccerPlayer("Son", "RW", 10)
print("현재 선수의 등번호는 : ", son.back_number)
print(son.__str__())
print(f"이름: {son.name}")
son.name = "Kane"
print(f"이름: {son.name}")
print(f"위치: {son.get_position()}")
print(f"위치: {son.position}")
son.set_position("CF")
print(f"위치: {son.get_position()}")
son.position = "CF"
print(f"위치: {son.position}")
son.__name = "kane"
print(son.name)