class SoccerPlayer(object):

    def __init__(self, name, position,back_number):
        self.__name = name
        self.__position = position
        self.__back_number = back_number


    def name(self):
        return self.__name

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        if new_position.isalpha():
            self.__position = new_position
        else:
            raise ValueError("알파벳만 사용하세요!")

    @property
    def back_number(self):
        return self.__back_number

    def __str__(self):
        return f"name:{self.__name}, position:{self.__position}, back_number:{self.__back_number}"

if __name__ == "__main__": # 실행모듈
    son = SoccerPlayer("Son", "RW", 10)
    print("현재 선수의 등번호는 : ", son.back_number)
    print(son.__str__())
    son.position = "GK"
    print(f"포지션은 {son.position} 입니다.")

    # def __str__(self):
    #     return "name:{}, position:{}, back_number:{}"\
    #         .format(self.name, self.position, self.back_number)
