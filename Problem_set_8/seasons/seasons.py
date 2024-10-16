from datetime import datetime
import sys
import inflect
p = inflect.engine()

def main():
    print(season(input("Date of Birth(YYYY-MM-DD): ")))


def season(birth_date):
    try:
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

        if birth_date > today:
            sys.exit("Invalid Date")

        days_gap = (today-birth_date).days

        ''''
        print(today)
        print(birth_date)
        print(days_gap)'''

        return p.number_to_words(int(days_gap)*24*60)


    except ValueError:
        sys.exit("Invalid Date Format")

if __name__ == "__main__":
    main()