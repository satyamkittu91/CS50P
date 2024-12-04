from datetime import date
import sys
import inflect
import re
p = inflect.engine()

def main():
    print(season(input("Date of Birth(YYYY-MM-DD): ")))

def season(bdate):
    if search := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", bdate):
        bdate = list(map(int, search.groups()))

    else:
        sys.exit("Invalid Date Format")

    if (bdate[1] < 1 or bdate[1] > 12) or (bdate[2] < 1 or bdate[2] > 31):
        sys.exit("Invalid Date")

    else:
        bdate = date(bdate[0], bdate[1], bdate[2])
        today = date.today()
        days_gap = (today-bdate).days
        min_word = p.number_to_words(int(days_gap)*24*60).capitalize().replace(" and ", ' ')
        return f"{min_word} minutes"

if __name__ == "__main__":
    main()
