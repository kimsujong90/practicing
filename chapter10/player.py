class SoccerPlayer(object):

    def __init__(self, name, position,back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    # def __str__(self):
    #     return "name:{}, position:{}, back_number:{}"\
    #         .format(self.name, self.position, self.back_number)


    def name(self):
        return self.name

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    def get_number(self):
        return self.back_number

    def __str__(self):
        return f"name:{self.name}, position:{self.position}, back_number:{self.back_number}"

if __name__ == "__main__": # 실행모듈
    son = SoccerPlayer("Son", "RW", 10)
    print("현재 선수의 등번호는 : ", son.back_number)
    print(son.__str__())
    print(type(son))

