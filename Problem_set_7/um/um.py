import re

def main():
    print(count(input("Text: ")))


def count(text):
    um = re.findall(r"\bum\b", text)
    return len(um)


if __name__ == "__main__":
    main()