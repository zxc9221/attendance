def get_attendance_day_of_week(path):
    attendance_info = []
    with open(path, encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            attendance_info.append((parts[0], parts[1]))
    return  attendance_info


def get_attendance_info(attendance_day_of_week):
    attendance_infos = {}
    for name, day_of_week in attendance_day_of_week:
        if name not in attendance_infos:
            attendance_infos[name] = {"point": 0, "wed" : 0, "weekend": 0}
        if day_of_week == "wednesday":
            attendance_infos[name]["point"] += 3
            attendance_infos[name]["wed"] += 1
        elif day_of_week in ["saturday", "sunday"]:
            attendance_infos[name]["point"] += 2
            attendance_infos[name]["weekend"] += 1
        else:
            attendance_infos[name]["point"] += 1
    return  attendance_infos


def update_bonus_point(attendance_infos):
    attendance_update_point_infos = attendance_infos
    for name in attendance_update_point_infos:
        if attendance_update_point_infos[name]["wed"] >= 10:
            attendance_update_point_infos[name]["point"] += 10
        if attendance_update_point_infos[name]["weekend"] >= 10:
            attendance_update_point_infos[name]["point"] += 10
    return attendance_update_point_infos


def update_grade(attendance_infos):
    attendance_update_point_infos = attendance_infos
    for name in attendance_infos:
        if attendance_update_point_infos[name]["point"] >= 50:
            attendance_update_point_infos[name]["grade"] = "GOLD"
        elif attendance_update_point_infos[name]["point"] >= 30:
            attendance_update_point_infos[name]["grade"] = "SILVER"
        else:
            attendance_update_point_infos[name]["grade"] = "NORMAL"
    return attendance_update_point_infos


def print_attendance(attendance_infos):
    for name in attendance_infos:
        print(f"Name : {name}, POINT : {attendance_infos[name]['point']}, GRADE : {attendance_infos[name]['grade']}")


def seletion_remove_player(attendance_infos):
    remove_player = []
    for name in attendance_infos:
        if attendance_infos[name]["grade"] == "NORMAL" and\
            attendance_infos[name]["wed"] == 0 and\
            attendance_infos[name]["weekend"] == 0:
            remove_player.append(name)
    return remove_player


def print_remove_player(remove_player):
    for player in remove_player:
        print(player)

