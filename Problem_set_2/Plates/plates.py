def main():
    plate = input("Input: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not s.isalnum():
        return False
    elif 2 > len(s) or len(s) > 6:
        return False
    elif not s[:2].isalpha():
        return False
    for char in s:

        if char.isdigit() and s.index(char) < len(s) - 1 and  s[s.index(char) + 1].isalpha():
            return False
        elif char.isalpha():
            continue
        elif "0" in s:
            if char == "0":
                a = s.index(char) - 1
                if s[a].isalpha():
                    return False
                else:
                    continue
            else:
                continue
    return True

if __name__ == "__main__":
    main()
