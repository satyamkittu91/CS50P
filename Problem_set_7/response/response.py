import validators

def main():
    if validators.email(input("What's your Email Address: ")):
        print("Valid")

    else:
        print("Invalid")


if __name__ == "__main__":
    main()