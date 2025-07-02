def Attendance_Checker(total_days,attended_days):
    if total_days <= 0:
        print("Number of days can't be zero or less than zero")

    attendance_percentage = (attended_days/total_days) * 100
    result = f"Your attendance is {attendance_percentage:.2f}%\n"

    if attendance_percentage >= 75:
        result += "You are eligible for according to attendance"
    else:
        result += "Your attendance is below than required percentage"
    return result

total_days = int(input("Enter total days in school: "))
attended_days = int(input("Enter attended days in school: "))
print(Attendance_Checker(total_days,attended_days))