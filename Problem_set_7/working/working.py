import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.search(r"^([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM) to ([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM)$", s):
        start_hour = time.group(1)
        start_minute = time.group(2)
        if start_minute == None:
            start_minute = ":00"
        start_period = time.group(3)

        end_hour = time.group(4)
        end_minute = time.group(5)
        if end_minute == None:
            end_minute = ":00"
        end_period = time.group(6)

        start_time = convert_to_24format(start_hour, start_minute, start_period)
        end_time = convert_to_24format(end_hour, end_minute, end_period)
    
        return f"{start_time} to {end_time}"
    
    else:
        raise ValueError


def convert_to_24format(hour, minute, period):
    hour = int(hour)
    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0
    
    return f"{hour:02}{minute}"



if __name__ == "__main__":
    main()