months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

input_date = input("Date: ").strip()

while True:
    try:
        if "/" in input_date:
            mm, dd, yyyy = input_date.split("/")
        elif "," in input_date:
            mmdd, yyyy = input_date.split(", ")
            mm, dd = mmdd.split(" ")
            mm = months.index(mm)
            mm = mm + 1
            if int(mm) > 12 or int(dd) > 31:
                raise ValueError
            else:
                print(f"{yyyy}-{mm:0>2}-{dd:0>2}")
        else:
            raise ValueError
    except (ValueError, KeyError, AttributeError, NameError):
        pass

