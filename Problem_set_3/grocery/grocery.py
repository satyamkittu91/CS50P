import sys
items = []
items.sort()
exiting = False
while True:
    try:
        item = input().title()
        items.append(item)
    except (KeyboardInterrupt, EOFError):
        exiting = True
        break

if exiting:
    #print("\n")
    items_name = set()
    for i in items:
        items_name.add(i)
    for item in items_name:
        a = items.count(item)
        print(f"{a} {item.upper()}", end='\n')
    sys.exit(0)
