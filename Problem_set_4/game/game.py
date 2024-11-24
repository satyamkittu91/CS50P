import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue
    else:
        if level > 0:
            break
        else:
            continue

random_word = int(random.choice(range(1, level)))

while True:
    try:

        guessed_word = int(input("Guess: "))
    except ValueError:
        continue
    else:
        if guessed_word < 0:
            continue
        else:



            if guessed_word > random_word:
                print("Too Large!")
                continue
            elif guessed_word < random_word:
                print("Too small!")
                continue
            elif guessed_word == random_word:
                print("Just Right!")
                break
            else:
                continue