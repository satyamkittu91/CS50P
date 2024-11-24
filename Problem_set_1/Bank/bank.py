greet = input("Greeting: ").strip().lower()

if "hello" in greet:
    print("$0")
elif 'h' in greet[0][0] and "hello" not in greet:
    print("$20")
else:
    print("$100")
