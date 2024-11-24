import random

def main():
    correct_answer = 0
    total_correct_answer = 0
    level = get_level()
    while correct_answer < 10:
        x, y = generate_integer(level)
        wrong_answer = 1
        while correct_answer < 10:
            try:
             answer = int(input(f"{x} + {y} = "))
            except ValueError:
                pass
            else:
                if answer == x + y:
                    correct_answer = correct_answer + 1
                    total_correct_answer = total_correct_answer + 1
                    break
                elif answer != x + y and wrong_answer < 3:
                    wrong_answer = wrong_answer + 1
                    print("EEE")
                else:
                    print(x+y)
                    correct_answer += 1
                    break
    print(f"Correct Answers {total_correct_answer}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except ValueError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x,y


if __name__ == "__main__":
    main()
