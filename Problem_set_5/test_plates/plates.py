def main():
    plate = input("Plate: ")
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
        if s[-1].isalpha() and char.isdigit():
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