def main():
    time = input("What time is it: ").strip()
    convert(time)

def convert(time):
    hour, minute = time.split(":")
    if hour == "7":
        print("breakfast time")
    elif hour == "8" and minute == "00":
        print("breakfast time")
    elif hour == "12":
        print("lunch time")
    elif hour == "13" and minute == "00":
        print("lunch time")
    elif hour == "18":
        print("dinner time")
    elif hour == "19" and minute == "00":
        print("dinner time")
    else:
        None
    
if __name__ == "__main__":
    main()