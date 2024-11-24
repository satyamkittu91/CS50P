import re

def main():
    print(count(input("Text: ").strip()))


def count(text):
    um = re.findall(r"\bum\b", text.lower())
    return len(um)


if __name__ == "__main__":
    main()