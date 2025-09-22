from os import remove

from attendance_book import AttendanceBook
from person import Person

class BaseBallAttendanceBook(AttendanceBook):
    def __init__(self):
        self.__remove_player = []
        self.__attendance_info = {}
        self.__id = 1

    def attendance(self, name, day_of_week):
        if name not in self.__attendance_info:
            self.__attendance_info[name] = Person(name, self.__id)
            self.__id += 1

        self.__attendance_info[name].update_attendance(day_of_week)
        self.__attendance_info[name].update_bonus_point(day_of_week)
        self.__attendance_info[name].update_grade()

    def get_remove_player(self):
        self.__remove_player = []
        for name in self.__attendance_info:
            if self.__attendance_info[name].is_remove_player():
                self.__remove_player.append(name)

    def print_attendance_info(self):
        for name in self.__attendance_info:
            print(f"Name : {name}, POINT : {self.__attendance_info[name].point}, GRADE : {self.__attendance_info[name].grade}")

    def print_remove_player(self):
        for player in self.__remove_player:
            print(player)
