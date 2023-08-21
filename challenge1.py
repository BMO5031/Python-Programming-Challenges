def convert_to_24_hour(hour, minute, period):
    if period == "am":
        if hour == 12:
            hour = 0
    elif period == "pm":
        if hour != 12:
            hour += 12
    return f"{hour:02d}:{minute:02d}"
print(convert_to_24_hour(8, 35, "pm"))
