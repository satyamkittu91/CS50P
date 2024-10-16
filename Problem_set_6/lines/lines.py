import sys


def main():
    check_cl_argument()

    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()

    except FileNotFoundError:
        sys.exit("File does not exist")

    else:
        count = 0
        for line in lines:
            if line.lstrip()[0] != r"#":
                count += 1

        print(count)        



def check_cl_argument():
    # check for the number of sys.argv
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many commnad-line arguments")
    #check if the command is a python file
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()