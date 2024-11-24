
def main():
    full_word = input("Input: ")
    print(shorten(full_word))



def shorten(word):
    shortned_word = ''
    for char in word:
        if char not in "aeiouAEIOU" and char.isalpha():
            shortned_word = shortned_word + char
    return shortned_word

if __name__ == "__main__":
    main()

