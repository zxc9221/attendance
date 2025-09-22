def get_attendance_day_of_week(path):
    attendance_info = []
    with open(path, encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            attendance_info.append((parts[0], parts[1]))
    return  attendance_info