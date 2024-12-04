import sys
items = []
items.sort()
exiting = False
while True:
    try:
        item = input().strip().upper()
        items.append(item)
    except (KeyboardInterrupt, EOFError):
        exiting = True
        break

if exiting:
    #print("\n")
    items_name = set()
    items_count = []
    item_dict = {}
    for i in items:
        items_name.add(i)
    items_name = list(items_name)
    for item in items_name:
        a = items.count(item)
        item_dict[item] = a

    item_sdict = sorted(item_dict.items(), key=lambda x: x[1], reverse=True)
    for i in item_sdict:
        print(f"{i[1]} {i[0]}")
        #items_count.append(a)
    '''
    items_count.sort(reverse=True)
    for i in items_count:
        item= items_name[items_count.index(i) - 1]
        print(f"{i} {item}")
        '''
    sys.exit(0)
