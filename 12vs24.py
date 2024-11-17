def convertTime(given_input):
    time = given_input
    str_hours = ""
    a = time.index(":")
    i = 0
    while time[i]!=":":
        str_hours += time[i]
        i += 1
    hours = int(str_hours)
# for 12 hours format into 24 hours format
    if "pm" in time or "am" in time:
        if "pm" in time and hours !=12:
            b = (hours+12)%24
            print(str(f"{b}{time[a:a+3]}"))
        elif "am" in time and hours==12:
            b = (hours+12)%24
            print(str(f"{b}{time[a:a+3]}"))
        else:
            print(str(f"{hours}{time[a:a+3]}"))
# for 24 hours format into 12 hours format
    else:
        if hours>12:
            b = (hours-12)
            print(str(f"{b}{time[a:a+3]} pm"))
        else:
            print(str(f"{hours}{time[a:a+3]} am"))
# convertTime(input("enter "))
convertTime("12:00 am")
convertTime("6:20 pm")
convertTime("21:00")
convertTime("5:05")