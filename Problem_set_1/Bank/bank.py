greet = input("Greeting: ")

if greet == "Hello" or greet == "hello":
    print("$0")
elif greet[0] in ["h", "H"] and greet.lower() != "hello":
    print("$20")
else:
    print("$100")