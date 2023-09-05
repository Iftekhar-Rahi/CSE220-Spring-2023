# import datetime
# a=input("Enter whether you are starting or ending: ").upper()
#
# if a=="S":
#     current_time = datetime.datetime.now()
#     starting_time=current_time.strftime("%H:%M:%S").split(":")
#
# a=input("Enter whether you are starting or ending: ").upper()
# if a=="E":
#     current_time = datetime.datetime.now()
#     ending_time=current_time.strftime("%H:%M:%S").split(":")
#
# total_time=f"{int(ending_time[0]) - int(starting_time[0])}:{int(ending_time[1]) - int(starting_time[1])}:{int(ending_time[2]) - int(starting_time[2])}"
# print(total_time)


import datetime

study_sessions = []

while True:
    a = input("Enter whether you are starting (S), ending (E), or done (D): ").upper()

    if a == "D":
        break

    current_time = datetime.datetime.now()

    if a == "S":
        starting_time = current_time
    elif a == "E":
        ending_time = current_time
        study_sessions.append((starting_time, ending_time))
    else:
        print("Invalid input")

total_study_time = datetime.timedelta()

for session in study_sessions:
    study_duration = session[1] - session[0]
    total_study_time += study_duration

total_seconds = total_study_time.total_seconds()
hours = int(total_seconds // 3600)
minutes = int((total_seconds % 3600) // 60)
seconds = int(total_seconds % 60)

print(f"Total study time: {hours} hours, {minutes} minutes, {seconds} seconds")
