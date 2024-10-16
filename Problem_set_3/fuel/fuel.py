def main():
    '''takes user input'''
    while True:
        x, y = input("Fraction: ").split("/")
        a = get_fracion(int(x), int(y))
        if a is not None:
            print(a)
            break


def get_fracion(x, y):
    '''do all the calculations regarding fuel'''
    try:
        precentage = x/y * 100
        if x > y:
            raise ValueError
        if precentage <= 1:
            return "F"
        elif precentage >= 99:
            return "E"
        else:
            return f"{precentage}%"
    except (ValueError, ZeroDivisionError):
        return None

if __name__ == '__main__':
    main()