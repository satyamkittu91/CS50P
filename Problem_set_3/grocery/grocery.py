items = []
while True:
    try:
        item = input("Item: ")
        items.append(item)
    except KeyboardInterrupt:
        break

print("\n")
goods = []
for i in items:
    a = items.count(i)
    if i not in goods:
        goods.append(i)

        print(f"{a}. {i}")