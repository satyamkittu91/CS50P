full_word = input("Input: ")

short_form = []

for char in full_word:
    if char in "aeiou":
        None
    else:
        short_form.append(char)

print("Output: ", end="")
for char in short_form:
    print(char, end="")