def main():
    '''takes user input'''
    while True:
        input = input("Fraction: ")
        a = get_fraction(input)
        if a is not None:
            print(a)
            break

    
    

def get_fraction(input):
    '''do all the calculations regarding fuel'''
    
    x, y = input.split("/")
    x = int(x)
    y = int(y)
    
    try:
        precentage = x/y * 100
        if x > y:
            raise ValueError
        if precentage <= 1:
            return "E"
        elif precentage >= 99:
            return "F"
        else:
            return f"{precentage}%"
    except (ValueError, ZeroDivisionError):
        return None

if __name__ == '__main__':
    main()