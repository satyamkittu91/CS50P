def main():
    '''takes user input'''
    while True:
        frac = input("Fraction: ").strip()
        a = get_fraction(frac)
        if a is not None:
            print(a)
            break




def get_fraction(input):
    '''do all the calculations regarding fuel'''




    try:
        x, y = input.split("/")
        x = int(x)
        y = int(y)
        precentage = x/y * 100
        if x > y:
            raise ValueError
        if precentage <= 1:
            return "E"
        elif precentage >= 99:
            return "F"
        else:
            return f"{int(round(precentage))}%"
    except: #(ValueError, ZeroDivisionError):
        return None

if __name__ == '__main__':
    main()
