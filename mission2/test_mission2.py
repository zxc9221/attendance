from codecs import BOM_BE

import pytest
from baseball_attendance_book import BaseBallAttendanceBook
from file_input import get_attendance_day_of_week

def test_get_attendance_info(capsys):
    expect_print = '''Name : Umar, POINT : 48, GRADE : SILVER
Name : Daisy, POINT : 45, GRADE : SILVER
Name : Alice, POINT : 61, GRADE : GOLD
Name : Xena, POINT : 91, GRADE : GOLD
Name : Ian, POINT : 23, GRADE : NORMAL
Name : Hannah, POINT : 127, GRADE : GOLD
Name : Ethan, POINT : 44, GRADE : SILVER
Name : Vera, POINT : 22, GRADE : NORMAL
Name : Rachel, POINT : 54, GRADE : GOLD
Name : Charlie, POINT : 58, GRADE : GOLD
Name : Steve, POINT : 38, GRADE : SILVER
Name : Nina, POINT : 79, GRADE : GOLD
Name : Bob, POINT : 8, GRADE : NORMAL
Name : George, POINT : 42, GRADE : SILVER
Name : Quinn, POINT : 6, GRADE : NORMAL
Name : Tina, POINT : 24, GRADE : NORMAL
Name : Will, POINT : 36, GRADE : SILVER
Name : Oscar, POINT : 13, GRADE : NORMAL
Name : Zane, POINT : 1, GRADE : NORMAL\n'''

    attendance_book = BaseBallAttendanceBook()
    attendance_day_of_week_info = get_attendance_day_of_week(f"./resource/attendance_weekday_500.txt")

    for name, day_of_week in attendance_day_of_week_info:
        attendance_book.attendance(name, day_of_week)
    attendance_book.print_attendance_info()
    out, _ = capsys.readouterr()
    assert expect_print == out

def test_get_remove_player(capsys):
    expect_print = "Bob\nZane\n"

    attendance_book = BaseBallAttendanceBook()
    attendance_day_of_week_info = get_attendance_day_of_week(f"./resource/attendance_weekday_500.txt")

    for name, day_of_week in attendance_day_of_week_info:
        attendance_book.attendance(name, day_of_week)
    attendance_book.get_remove_player()
    attendance_book.print_remove_player()
    out, _ = capsys.readouterr()

    assert expect_print == out

