
rhyme = "Adieu, adieu, to,"
list_of_names = []
while True:

    try:
        a = input("Name: ")
        list_of_names.append(a)
    except EOFError:
        break

local_list = []

for name in list_of_names:
    local_list.append(name)

    if len(local_list) == 1:
        print(rhyme + " " + local_list[0])
    elif len(local_list) == 2:
        print(rhyme + " " + local_list[0] + ", And " + local_list[1])
    else:
        print(rhyme + " " +  " , ".join(local_list[0:(len(local_list) - 1)]) + " And " + local_list[-1])