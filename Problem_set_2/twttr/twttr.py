
def main():
    full_word = input("Input: ")
    print(shorten(full_word))


def shorten(word):
    for char in word:
        if char in "aeiouAEIOU":
            word = word.replace(char, '')
    return word

if __name__ == "__main__":
    main()

