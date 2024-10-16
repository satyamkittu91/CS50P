import sys
from tabulate import tabulate
import csv

def main():

    check_cl_argument()
    table = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
            print(tabulate(table[1:], headers=table[0], tablefmt='grid'))

    except FileNotFoundError:
        sys.exit("File does not exist")



def check_cl_argument():
    # check for the number of sys.argv
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many commnad-line arguments")
    #check if the command is a csv file
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()