class Person():
    def __init__(self, name, id):
        self.__name = name
        self.__point = 0
        self.__wed = 0
        self.__weekend = 0
        self.__grade = "NORMAL"
        self.__back_number = id

    def update_attendance(self, day_of_week):
        if day_of_week == "wednesday":
            self.__point += 3
            self.__wed += 1
        elif day_of_week in ["saturday", "sunday"]:
            self.__point += 2
            self.__weekend += 1
        else:
            self.__point += 1

    def update_bonus_point(self, day_of_week):
        if day_of_week == "wednesday" and self.__wed == 10:
            self.__point += 10
        elif day_of_week in ["saturday", "sunday"] and self.__weekend == 10:
            self.__point += 10

    def update_grade(self):
        if self.__point >= 50:
            self.__grade = "GOLD"
        elif self.__point >= 30:
            self.__grade = "SILVER"

    def is_remove_player(self):
        return True if self.__grade == "NORMAL" and self.__wed == 0 and self.__weekend == 0 else False

    @property
    def point(self):
        return self.__point

    @property
    def grade(self):
        return self.__grade

