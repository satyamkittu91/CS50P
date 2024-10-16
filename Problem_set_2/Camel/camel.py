def main():
    a = input("camelCase: ")
    result = camel_to_snake(a)
    print(f"snake_case: {result}")

def camel_to_snake(camelCase):
    b = []
    for char in camelCase:
        if char.islower():
            b.append(char)
        else:
            b.extend(['_', char.lower()])

    return ''.join(b)

if __name__ == "__main__":
    main()