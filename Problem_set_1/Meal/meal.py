def main():
    time = input("What time is it: ").strip()

    time = str(convert(time)).split(".")
    if time[0] == "7":
        print("breakfast time")
    elif time[0] == "8":
        print("breakfast time")
    elif time[0] == "12":
        print("lunch time")
    elif time[0] == "13":
        print("lunch time")
    elif time[0] == "18":
        print("dinner time")
    elif time[0] == "19":
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    hour, minute = int(hour), int(minute)
    return hour + minute/60

if __name__ == "__main__":
    main()
