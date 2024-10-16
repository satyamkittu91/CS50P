x, y, z = input("Expression: ").strip().split(" ")

num1 = float(x)
num2 = float(z)

if y == "+":
    print(num1+num2)
elif y == "-":
    print(num1-num2)
elif y == "*":
    print(num1*num2)
elif y == "/":
    print(num1/num2)
else:
    print("Enter a valid statement.")