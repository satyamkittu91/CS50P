def main():
    greet = input("Greeting: ")
    print(pay())

def pay(greet):

    if greet == "Hello" or greet == "hello":
        return "$0"
    elif greet[0] in ["h", "H"] and greet.lower() != "hello":
        return "$20"
    else:
        return "$100"

