menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
order_list = []

def main():
    while True:
        try:
            order = input("Item: ")
            for key,value in menu.items():
                if key == order:
                    order_list.append(value)
            
            sum = 0
            for i in order_list:
                sum = sum + i
            print(f"Total: {sum}$")
        except KeyboardInterrupt:
            break






if __name__ == "__main__":
    main()