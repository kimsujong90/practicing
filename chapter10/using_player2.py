import player2

son = player2.SoccerPlayer("Son", "RW", 10)

son._SoccerPlayer__name = "kane"
print((son.position))
print(son._SoccerPlayer__name)
print(son.name())
son.position = "GK"
print(f"위치: {son.position}")