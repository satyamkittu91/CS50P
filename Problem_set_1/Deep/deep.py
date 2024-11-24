ft = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

if ft.strip().lower() in ["42", "forty two", "forty-two"]:
    print("Yes", end='')
else:
    print("No", end='')
