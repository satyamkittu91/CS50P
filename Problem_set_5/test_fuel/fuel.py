def main():
    '''takes user input'''
    while True:
        try:
            frac = input("convert: ").strip()
            a = convert(frac)
        except:
            pass
        else:
            break
        a = gauge(a)
        print(a)




def convert(input):
    '''do all the calculations regarding fuel'''

    x, y = input.split("/")
    x = int(x)
    y = int(y)
    percentage = x/y * 100
    if x > y:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    else:
        return int(round(percentage))

def gauge(percentage):
    
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == '__main__':
    main()
